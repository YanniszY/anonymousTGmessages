import asyncio
import random
import string

import redis.asyncio as redis
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from config import BOT_TOKEN
from States.states import UserMessage

redis = redis.from_url('redis://localhost')

bot = Bot(BOT_TOKEN)
router = Router()

async def generate_unique_code(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@router.message(CommandStart())
async def start_handler(message: types.Message, state: FSMContext):
    if message.text and len(message.text.split()) > 1:
        unique_code = message.text.split()[1]
        user_id = await redis.get(unique_code)

        if user_id:
            user_id = int(user_id.decode('utf-8'))
            await state.update_data(user_id=user_id)
            await state.set_state(UserMessage.message)
            await message.answer("Напиши анонимное сообщение")
        else:
            await message.answer("Неверная или устаревшая ссылка!")
    else:
        unique_code = await generate_unique_code()
        await redis.set(unique_code, message.from_user.id)
        unique_link = f"https://t.me/Ttydydhdi_bot?start={unique_code}"
        await message.answer(f"""
Привет! Это бот для анонимных сообщений.\n
Твоя ссылка: {unique_link}\n
Поставь ее себе в профиль чтобы люди перешевшие
по этой ссылке смогли отправить тебе анонимное сообщение!
\n
И не забывай про вежливость!
""")

@router.message(UserMessage.message)
async def get_text_message(message: Message, state: FSMContext):
    data = await state.get_data()
    user_id = data.get('user_id')
    user_message = message.text

    if user_id and user_message:
        await send_message(user_id, user_message)
        await message.answer("Ваше сообщение отправлено!")
    else:
        await message.answer("Произошла ошибка, попробуйте снова.")

    await state.clear()

async def send_message(user_id, user_message):
    await bot.send_message(chat_id=user_id, text="Получено новое сообщение!")
    await bot.send_message(chat_id=user_id, text=f"Анонимное сообщение: {user_message}")




async def main():
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

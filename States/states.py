from aiogram.fsm.state import State, StatesGroup


class UserMessage(StatesGroup):
    message = State()
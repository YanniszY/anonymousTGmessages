# Anonymous Telegram Bot

This project is a Telegram bot that generates a unique link for each user. Users can share these links to receive anonymous messages from anyone.

## Description

**Anonymous Telegram Bot** allows users to get a unique link that can be shared on social media, forums, or sent directly to others. Anyone with access to this link can send an anonymous message, which will be safely delivered right to the link owner's Telegram.

![logo](img/logo.png)

### Key Features

- **Unique Link Generation**: Creates a distinct link for every registered user.
- **Anonymous Messaging**: Seamless message delivery through generated links.
- **Privacy & Security**: Send messages with complete sender anonymity.
- **User-Friendly**: Easy setup and interaction directly within Telegram.

## Installation & Setup

### Requirements

- Python 3.12+
- Redis Server
- Telegram Bot API Token

### Installation Steps

1. Clone the repository and navigate to the project directory:

```bash
    git clone [https://github.com/YanniszY/anonymousTGmessages.git](https://github.com/YanniszY/anonymousTGmessages.git)
    cd anonymousTGmessages
```

2. Install the required dependencies:

```bash
    pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your Telegram Bot API token:

```env
    BOT_TOKEN="your_bot_token_here"
```

4. Start your Redis server:
```bash
    redis-server
```

5. Run the bot script:

```bash
    python bot.py
```

## How to Use

1. Start the bot in Telegram.
2. Use the `/start` command to generate your unique link.
3. Share this link anywhere (Instagram bio, Twitter/X, TikTok, etc.).
4. Receive anonymous feedback and messages directly in your Telegram chat!

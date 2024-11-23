# Discord Bot

This is a simple Discord bot written in Python using the `discord.py` library. The bot responds to specific messages in a Discord server.

## Features

- Logs a message when the bot is ready.
- Responds to messages that start with `$hi`.

## Prerequisites

- Python 3.8 or higher
- `discord.py` library
- `python-dotenv` library

## Setup

1. **Clone the repository**:
2. 
   ```sh
   git clone (https://github.com/PrathamX595/First-Discord-Bot.git)
   cd your-directory
   ```
3. **Install the required libraries**:
   ```sh
   pip install discord.py python-dotenv
   ```
4. **Create a .env file**: Create a .env file in the root directory of your project and add your bot token:
   ```sh
   TOKEN=your-bot-token
   ```
5. **Enable Privileged Intents**:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Select your application.
   - Navigate to the "Bot" section.
   - Enable the "Message Content Intent" under "Privileged Gateway Intents".
   - Save changes.
     
## Running the Bot
Run the bot using the following command:
```sh
python main.py
```

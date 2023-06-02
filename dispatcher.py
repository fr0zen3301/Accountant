import logging
from aiogram import Bot, Dispatcher
import bot_token
from aiogram import md
# Configure logging
logging.basicConfig(level=logging.INFO)

# prerequisites
if not bot_token.BOT_TOKEN:
    exit("No token provided")

# init
bot = Bot(token=bot_token.BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)

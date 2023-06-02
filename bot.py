from aiogram import executor
from dispatcher import dp
import handlers

from database import BotDB
BotDB = BotDB('accountant.db')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True) # False if we don't worry about client's information

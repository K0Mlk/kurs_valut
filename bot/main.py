import os
import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from handlers import cmd_start, cmd_exchange, cmd_rates

load_dotenv()
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


dp.message.register(cmd_start, Command("start"))
dp.message.register(cmd_exchange, Command("exchange"))
dp.message.register(cmd_rates, Command("rates"))


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
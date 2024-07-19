import os
import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums import ParseMode

load_dotenv()
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"Zdarova! <b>{message.from_user.full_name}</b>",
        parse_mode=ParseMode.HTML
        )


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
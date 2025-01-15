import asyncio
import logging
from datetime import datetime

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import TOKEN

from app.handlers import router

#Объект бота
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")

async def main():
    dp.include_router(router)
    await dp.start_polling(bot, my_list = [1, 2, 3])

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
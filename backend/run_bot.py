import asyncio
import sys
import logging
from aiogram import Bot, Dispatcher
from app.core.config import settings
from app.bot.handlers import router

# fix for windows asyncio error
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def main():
    logging.basicConfig(level=logging.INFO)
    
    bot = Bot(token=settings.telegram_bot_token)
    dp = Dispatcher()
    
    # register handlers
    dp.include_router(router)

    print("--- BOT STARTED ---")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
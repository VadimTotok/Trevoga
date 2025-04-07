import asyncio
import logging

from telethon import TelegramClient

from . import config
from .bot import register_handlers

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

async def main():
    client = TelegramClient("session_name", config.API_ID, config.API_HASH)
    try:
        await client.start()
        logging.info("Бот запущен и ожидает сообщений :^)")
        register_handlers(client)
        await client.run_until_disconnected()
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")
    finally:
        await client.disconnect()
        logging.info("Бот остановлен")

if __name__ == "__main__":
    asyncio.run(main())

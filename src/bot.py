import logging

from telethon import TelegramClient, events

from . import config
from .utils import send_alert

def register_handlers(client: TelegramClient):
    @client.on(events.NewMessage(chats=config.CHANNEL_ID))
    async def normal_handler(event):
        message_text = event.message.message
        logging.info(f"Получено сообщение из канала: {message_text}")

        if config.TURN_ON_KEYWORD in message_text.casefold():
            await send_alert(client, config.TARGET_CHANNEL_ID, "Ракетная опасность")

        if config.TURN_OFF_KEYWORD in message_text.casefold():
            await send_alert(client, config.TARGET_CHANNEL_ID, "Отбой ракетной опасности")

        logging.info("Обработчики событий зарегистрированы")

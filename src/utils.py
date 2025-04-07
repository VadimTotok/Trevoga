import logging

from telethon import TelegramClient

async def send_alert(client: TelegramClient, target_channel_id: str, message: str):
    try:
        await client.send_message(target_channel_id, message)
        logging.info(f"Сообщение '{message}' отправлено в канал {target_channel_id}")
    except Exception as e:
        logging.error(f"Ошибка при отправке сообщения в канал: {e}")

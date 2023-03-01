# This code is written by TheTaemAlexa 
import telegram
from typing import Callable, Union, Optional
from pyrogram import Client
from pyrogram.types import Message, CallbackQuery

OWNER_ID = 6174058850


def bot_creator(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in OWNER_ID:
            return await func(client, message)
@bot_creator
def send_to_all_groups(update, context):
    message_text = ' '.join(context.args)
    for chat in bot.getUpdates():
        if chat.message.chat.type == 'group':
            bot.send_message(chat_id=chat.message.chat_id, text=message_text)
send_to_all_groups_handler = CommandHandler('gcast', send_to_all_groups)
dispatcher.add_handler(send_to_all_groups_handler)

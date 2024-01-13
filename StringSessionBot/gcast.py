# This code is written by TheTaemAlexa on Jan 13, 2024

from pyrogram import Client, filters
from pyrogram.types import Message

            
owner_id = 6174058850
user_ids = {}


@Client.on_message(filters.command("gcast") & filters.private)
def gcast_command(client, message):
    if message.from_user.id == owner_id:
        users = client.get_chat_members(message.chat.id)
        message.reply_text("Enter the message you want to broadcast:")
        client.register_message_handler(handle_broadcast, (filters.text & filters.private), state=users)
    else:
        message.reply_text("You are not authorized to use this command.")

def handle_broadcast(client, message):
    users = message.text.split('\n')
    delivered_count = 0
    
    for user_id in users:
        try:
            user_id = int(user_id)
            client.send_message(user_id, "Broadcast message By @TheTeamAlexa: " + message.text)
            user_ids[user_id] = message.chat.id
            delivered_count += 1
        except ValueError:
            pass
    message.reply_text(f"Broadcast sent successfully to {delivered_count} users/chats!")

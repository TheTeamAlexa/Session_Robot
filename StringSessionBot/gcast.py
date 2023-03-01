# This code is written by TheTaemAlexa
from pyrogram import Client, filters


@Client.on_message(filters.user(6174058850) & filters.command("gcast"))
def send_to_all_groups(client, message):
    message_text = " ".join(message.command[1:])
    for chat in client.iter_dialogs():
        if chat.chat.type == "group":
            client.send_message(chat.chat.id, text=message_text)

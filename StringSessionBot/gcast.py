# This code is written by TheTeamAlexa

import pickledb
from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message

# Initialize the database
db = pickledb.load("user_db.db", False)


# Filters to use command
def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)


# Owner id
owner_id = 6174058850


# Start Message
@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    user = await bot.get_me()
    user_id = msg.from_user.id
    if not db.exists(str(user_id)):
        db.set(str(user_id), True)
    mention = user.mention
    await bot.send_message(
        msg.chat.id,
        Data.START.format(msg.from_user.mention, mention),
        reply_markup=InlineKeyboardMarkup(Data.buttons),
    )


@Client.on_message(filter("gcast") & filters.private)
async def broadcast_command(client, message):
    if message.from_user.id == owner_id:
        await message.reply_text("Enter the message you want to broadcast:")
        broadcast_text = message.text.split(" ", 1)[1]
        delivered_count = 0
        for user_id in db.getall():
            try:
                user_id = int(user_id)
                await client.send_message(
                    user_id, f"Broadcast message By @TheTeamAlexa: {broadcast_text}"
                )
                delivered_count += 1
            except ValueError:
                pass

        await client.send_message(
            message.chat.id, f"Broadcast sent successfully to {delivered_count} users!"
        )
    else:
        await message.reply_text("You are not authorized to use this command.")

from pyrogram import Client, filter
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram.types import CallbackQuery
# mport randam
import os

"""
PHOTO_LINK = [
 "Photo Link",
 "photo Link"
 ]"""

Dz = Client(
    "Dz",
    bot_token = os.environ.get("BOT_TOKEN", "6381483867:AAEAT3PbP7h5cejrgyb8e6wKP3gO0KshmvQ"),
    api_id = int(os.environ.get("API_ID", "29855436")),
    api_hash = os.environ.get("API_HASH", "c01b59b1d686c55d60a92c171e2b19fe",
)


@Dz.on_message(filters.command("start")) 
async def start(bot, message):
    buttons = [[
      InlineKeyboardButton("Mo Tech YT", callback_data="start")
      ]]
    await messages.reply_photo(
        photo=random.choice(PHOTO_LINK),
        text="Hello {message.from_user.mention}   Bro Sugamano",
        reply_markup=InlineKeyboardMarkup(buttons)
    )



@Muhammad.on_callback_query()
async def callback(bot, msg: CallbackQuery)
    if msg.data == "start":
        await message.message.edit(
            text=" hello {msg.from_user.mention}  Start Text"
        )



 Muhammed.run()

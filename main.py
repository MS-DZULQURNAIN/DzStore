from pyrogram import Client, filter
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
# mport randam
import os

OWNER = 1814359323

"""
PHOTO_LINK = [
 "Photo Link",
 "photo Link"
 ]"""

Dz = Client(
    "Dz",
    bot_token = os.environ.get("BOT_TOKEN", "6381483867:AAEAT3PbP7h5cejrgyb8e6wKP3gO0KshmvQ"),
    api_id = int(os.environ.get("API_ID", "29855436")),
    api_hash = os.environ.get("API_HASH", "c01b59b1d686c55d60a92c171e2b19fe"),
)


@Dz.on_message(filters.command("start")) 
async def start(bot, message):
    buttons = InlineKeyboardMarkup([
      [
       InlineKeyboardButton("OWNER", url=f"tg://user?id={OWNER}"),
      ],
      [
       InlineKeyboardButton("Menu", callback_data="menu"),
       InlineKeyboardButton("Help", callback_data="help"),
      ]
      [
       InlineKeyboardButton("Tutup", callback_data="close"),
      ]])
    mention = message.from_user.mention
    await message.reply_text(
        #photo=random.choice(PHOTO_LINK),
        text=f"**Hallo {mention}\n\nSaya Adalah DzStore tempat jajan telegram atau jajanan lain nya, silahkan pilih menu untuk menelusuri nya**",
        reply_markup=buttons,
        disable_web_page_preview=True
 )

print("AKTIF🔥")
Dz.run()

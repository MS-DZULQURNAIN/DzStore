from pyrogram import Client, filter
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram.types import CallbackQuery
# mport randam
import os

OWNER = [1814359323]

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
       InlineKeyboardButton("OWNER", url=f"tg://userid?{OWNER}"),
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
        text=f"Hallo {mention}\n\nSaya Adalah DzStore tempat jajan telegram atau jajanan lain nya, silahkan pilih menu untuk menelusuri nya",
        reply_markup=buttons
    )



@Dz.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    if msg.data == "menu":
        mention = msg.from_user.mention
        buttons = InlineKeyboardMarkup([
                              [
                                   InlineKeyboardButton("NOKOS", callback_data="nokos"),
                              ], 
                              [    
                                   InlineKeyboardButton("kembali", callback_data="home"),
                              ]])
        await msg.edit_inline_text(
            text=f"Halo {mention}\nMau jajan apa nih?",
            reply_markup=buttons
        )
    if msg.data == "nokos":
     buttons = InlineKeyboardMarkup([
                            [
                               InlineKeyboardButton("Admin", url=f"tg://userid?{OWNER}"),
                               InlineKeyboardButton("info...", url="t.me/DezetStore"),
                            ],
                            [
                               InlineKeyboardButton("kembali", callback_data="menu"),
                            ],
                       ])
     await msg.edit_inline_text(
      text="""
      NOKOS TELEGRAM ✅
      ID 1 Rp 40.000🇮🇩
      ID 2 Rp 35.000🇮🇩
      ID 8 / 9 PC ONLY
      ID FRESH 5 / 6 Rp 5.000🇮🇩

      Note:Tanyakan stock sebelum pay
      """, reply_markup=buttons)


print("AKTIF🔥")
Dz.run()

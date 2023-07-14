import os
import *
from main import Dz
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import filters, Message


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

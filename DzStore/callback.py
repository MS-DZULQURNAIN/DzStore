import os
import *
from main import Dz, OWNER
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import filters, Message
from DzStore.text import NOKOS, NOKOS1, NOKOS_DANA1, NOKOS_CONF_DANA1

npilih = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("ID 1", callback_data="np1"),
        InlineKeyboardButton("ID 2", callback_data="np2"),
        InlineKeyboardButton("Fresh", callback_data="npfresh"),
    ],


npc = [
        InlineKeyboardButton("Metode Pembayaran💳", callback_data="npay"),
    ]
])

npc2 = [
        InlineKeyboardButton("Metode Pembayaran💳", callback_data="npay2"),
    ]
])

npc3 = [
        InlineKeyboardButton("Metode Pembayaran💳", callback_data="npay3"),
    ]
])

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
                               InlineKeyboardButton("Masukan Keranjang🛒", callback_data="npilih"),
                            [
                               InlineKeyboardButton("kembali", callback_data="menu"),
                            ],
                       ])
     await msg.edit_inline_text(
      text=NOKOS,
      reply_markup=buttons)
    if msg.data == "npilih":
      await msg.edit_inline_text(
          text=NOKOS,
          reply_markup=npilih + npc
      )
    if msg.data == "np1":
      await msg.edit_inline_text(
          text=NOKOS1,
          reply_markup=npilih + npc
      )
    if msg.data == "npay":
      await msg.edit_inline_text(
          text=NOKOS_DANA1,
          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Konfirmasi Pembayaran ✅", callback_data="npdana")]])
      )
    if msg.data == "npdana":
      await msg.edit_inline_text(
          text=NOKOS_CONF_DANA1,
      )




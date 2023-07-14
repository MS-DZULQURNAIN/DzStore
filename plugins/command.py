from pyrogram import filters, Client, Message
from pyrogram.types import 
import *
from main import *

ADMIN_ID = "1814359323"

@Dz.on_message(filters.command("admin_topup"))
def admin_topup_command(bot: client, m: message):
    if m.from_user.id != ADMIN_ID:
        await bot.send_message(m.chat.id, "Anda tidak memiliki izin untuk melakukan top-up.")
        return
    # Mendapatkan argumen jumlah top-up dari pesan pengguna
    args = message.text.split()
    if len(args) < 2:
        await bot.send_message(m.chat.id, "Format perintah salah. Gunakan: /topup [jumlah]")
        return

    try:
        amount = float(args[1])
    except ValueError:
        await bot.send_message(m.chat.id, "Jumlah top-up harus berupa angka.")
        return

    # Memanggil fungsi add_topup() untuk menambahkan data top-up
    user_id = message.from_user.id
    add_topup(user_id, amount)

    await bot.send_message(m.chat.id, f"Top-up berhasil. Jumlah top-up: {amount}")

@Dz.on_message(filters.command("request_topup"))
async def request_topup_command(bot: client, m: message):
    # Mengirim permintaan top-up ke admin
    admin_id = ADMIN_ID
    await bot.send_message(admin_id, f"Permintaan top-up dari pengguna {m.from_user.id}. Jumlah top-up yang diminta: {amount}")
    await bot.send_message(m.chat.id, "Permintaan top-up telah dikirim ke admin.")

from pyrogram import Client, filters
from pyrogram.types import Message

# Definir el token del bot
API_ID = 23104177       # Reemplaza con tu API_ID
API_HASH = "ac8ae4a1c826c13e95936b912e2a09dd" # Reemplaza con tu API_HASH
BOT_TOKEN= "5818205719:AAHk-liE0DD4S5ltg-kFN88Ckn4CTBUmMNc"

# Crear una instancia del cliente Pyrogram
bot = Client("@LastHopePrueba_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start") & filters.private)
def cmd_start(bot, message):
    bot.send_message(message.chat.id, "Hola :D")

bot.run()
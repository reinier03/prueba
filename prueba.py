from pyrogram import Client, filters
from pyrogram.types import Message
import os



API_ID = os.environ.get("API_ID")       
API_HASH = os.environ.get("API_HASH") 
BOT_TOKEN= os.environ.get("TELEGRAM_TOKEN_BOT")

# Crear una instancia del cliente Pyrogram
bot = Client("@LastHopePrueba_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start") & filters.private)
def cmd_start(bot, message):
    bot.send_message(message.chat.id, "Hola :D")

bot.run()


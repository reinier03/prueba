from pyrogram import Client, filters
from pyrogram.types import Message
import os
from flask import Flask, request
from waitress import serve


API_ID = os.environ.get("API_ID")       
API_HASH = os.environ.get("API_HASH") 
BOT_TOKEN= os.environ.get("TELEGRAM_TOKEN_BOT")

# Crear una instancia del cliente Pyrogram
bot = Client("@LastHopePrueba_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start") & filters.private)
def cmd_start(bot, message):
    bot.send_message(message.chat.id, "Hola :D")

web_server= Flask(__name__)

@web_server.route("/", methods=["POST"])
def webhook():
    update = request.get_json()
    bot.process_update(update)
    return "OK"

def iniciar_webhook():
    bot.set_webhook(url=os.environ.get("URL"))
    serve(web_server, host="0.0.0.0", port=int(os.environ.get('PORT')))


iniciar_webhook()




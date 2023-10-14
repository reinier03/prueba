import telebot
import os
from flask import Flask, request
from waitress import serve
import time

bot=telebot.TeleBot("5818205719:AAHk-liE0DD4S5ltg-kFN88Ckn4CTBUmMNc")
web_server= Flask(__name__)

bot.set_my_commands([
    telebot.types.BotCommand("/start", "Da la bienvenida, o algo así")
])


@bot.message_handler(commands=["start"])
def cmd_star(message):
    bot.send_message(message.chat.id, "Esto es un mensaje de prueba")
    
@bot.message_handler(func=lambda x: True)
def cmd_recibir_mensajes(message):
    bot.send_message(message.chat.id, "El bot funciona")

bot.send_message(1413725506, "Estoy online :D")

@web_server.route("/", methods=["POST"])
def webhook():
    if request.headers.get("content-type") == "aplication/json":
        update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
        bot.process_new_updates([update])
        return "OK", 200
    
def iniciar_webhook():
    bot.remove_webhook()
    time.sleep(1)
    bot.set_webhook(url="https://api.render.com/deploy/srv-ckf54q6afg7c73fo3bb0?key=KJ29aU6GkhI")
    serve(web_server, host="0.0.0.0", port=int(os.environ.get('PORT', 80)))

iniciar_webhook()


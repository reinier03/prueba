import telebot
import os


bot=telebot.TeleBot("5818205719:AAHk-liE0DD4S5ltg-kFN88Ckn4CTBUmMNc")

@bot.message_handler(commands=["start"])
def cmd_star(message):
    bot.send_message(message.chat.id, "Esto es un mensaje de prueba")
    
@bot.message_handler(func=lambda x: True)
def cmd_recibir_mensajes(message):
    bot.send_message(message.chat.id, "El bot funciona")
    

bot.infinity_polling()

import telebot

bot=telebot.TeleBot("6685078171:AAErSR82jBZkpLfgFX4Y7nbEeZ6sYjs7AO8")

@bot.message_handler(commands=["start"])
def cmd_star(message):
    bot.send_message(message.chat.id, "Esto es un mensaje de prueba")
    
@bot.message_handler(func=lambda x: True)
def cmd_recibir_mensajes(message):
    bot.send_message(message.chat.id, "El bot funciona")
    

bot.infinity_polling()
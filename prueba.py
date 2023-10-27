from flask import Flask, request
from waitress import serve
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
import time
import threading


#-----------------------------Variables necesarias--------------------------
bot=telebot.TeleBot(os.environ.get('TELEGRAM_TOKEN_BOT'))
Reima=1413725506
directorio_actual=os.path.dirname(os.path.abspath(__file__))
#---------------------------------------------------------------------------

web_server= Flask(__name__)

@bot.message_handler(commands=["start"])
def cmd_start(message):
    bot.reply_to(message, "HOLA :D \nLo sentimos, este bot no es interactuable, sólo sirve para botonera :(")


if os.name=="nt":
    last_botonera=open(f"{directorio_actual}\\Last_Botonera.jpg", "rb")
else:
    last_botonera=open(f"{directorio_actual}//Last_Botonera.jpg", "rb")

def iniciar_bucle():
    while True:
        last_botonera.seek(0)
        #comprobar si el so es windows
        if os.name=='nt':
            if os.path.isfile(f"{directorio_actual}\\archivo_canales.txt"):
                botonera=InlineKeyboardMarkup(row_width=1)
                with open(f"{directorio_actual}\\archivo_canales.txt", "r+") as archivo:
                    archivo.seek(0)
                    lineas=archivo.readlines()
                    for linea in lineas:
                        botonera.add(InlineKeyboardButton(bot.get_chat(linea.strip()).title, url=f"https://t.me/{bot.get_chat(linea.strip()).username}"))
    
                        if not bot.get_chat_member(chat_id=linea.strip(), user_id=bot.user.id).status=="administrator":
                            bot.send_message(1413725506, f"<u>ATENCION!</u>:\nNO soy admin en @{bot.get_chat(linea.strip()).username}, ID: {linea.strip()}", parse_mode="html")
                    botonera.add(InlineKeyboardButton("(☞ﾟヮﾟ)☞ UNIRSE AQUÍ ☜(ﾟヮﾟ☜)", "https://t.me/LastHopePosting/25366"))
                    archivo.seek(0)
                    for e,linea in enumerate(lineas, start=0):
                        last_botonera.seek(0)
                        try:
                            msg=bot.send_photo(linea.strip(), last_botonera, caption="¡Si!, ¡Es eso mismo que estás pensando!\n Literalmente, <b>La Última Botonera</b> baby (☞ﾟヮﾟ)☞ ☜(ﾟヮﾟ☜)\n\n¡Oye Juan! ¿Quién hizo ese logo? ¡Quiero tatuarme eso en el c*lo!", parse_mode="html" , reply_markup=botonera)
                        except:
                            continue
            #si el archivo de texto no existe    
            else:
                if os.name=="nt":
                    bot.send_message(Reima, "No había archivo de texto con los canales\nProcederé a crearlo")
                    with open(f"{directorio_actual}\\archivo_canales.txt", "w") as archivo:
                        archivo.write("-1001161864648\n")
                else:
                    bot.send_message(Reima, "No había archivo de texto con los canales\nProcederé a crearlo")
                    with open(f"{directorio_actual}//archivo_canales.txt", "w") as archivo:
                        archivo.write("-1001161864648\n")

        #Si no se ejecuta en Windows sino que en Linux (o Mac)
        else:
            if os.path.isfile(f"{directorio_actual}//archivo_canales.txt"):
                botonera=InlineKeyboardMarkup(row_width=1)
                with open(f"{directorio_actual}//archivo_canales.txt", "r+") as archivo:
                    archivo.seek(0)
                    lineas=archivo.readlines()
                    for linea in lineas:
                        botonera.add(InlineKeyboardButton(bot.get_chat(linea.strip()).title, url=f"https://t.me/{bot.get_chat(linea.strip()).username}"))

                        if not bot.get_chat_member(chat_id=linea.strip(), user_id=bot.user.id).status=="administrator":
                            bot.send_message(1413725506, f"<u>ATENCION!</u>:\nNO soy admin en @{bot.get_chat(linea.strip()).username}, ID: {linea.strip()}", parse_mode="html")
                    botonera.add(InlineKeyboardButton("(☞ﾟヮﾟ)☞ UNIRSE AQUÍ ☜(ﾟヮﾟ☜)", "https://t.me/LastHopePosting/25366"))
                    archivo.seek(0)
                    for e,linea in enumerate(lineas, start=0):
                        last_botonera.seek(0)
                        try:
                            bot.send_photo(linea.strip(), last_botonera, caption="¡Si!, ¡Es eso mismo que estás pensando!\n Literalmente, <b>La Última Botonera</b> baby (☞ﾟヮﾟ)☞ ☜(ﾟヮﾟ☜)\n\n¡Oye Juan! ¿Quién hizo ese logo? ¡Quiero tatuarme eso en el c*lo!", parse_mode="html" , reply_markup=botonera)
                        except:
                            continue
            #si el archivo de texto no existe    
            else:
                bot.send_message(Reima, "No había archivo de texto con los canales\nProcederé a crearlo")
                with open(f"{directorio_actual}//archivo_canales.txt", "w") as archivo:
                    archivo.write("-1001161864648\n")
        tiempo=1800
        bot.send_message(Reima, f"La botonera volverá a ser publicada a las {time.strftime('%H:%M', time.localtime(time.time()+tiempo))}")
        bot.send_message(-1001161864648, f"La Botonera volverá a ser publicada a las {time.strftime('%H:%M', time.localtime(time.time()+tiempo))}")
        time.sleep(tiempo)


hilo_bucle=threading.Thread(name="hilo_bucle", target=iniciar_bucle)
hilo_bucle.start()

try:
    bot.remove_webhook()
    bot.delete_webhook()
except:
    pass

bot.polling()
from flask import Flask, request
from waitress import serve
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
import time
import threading

#-----------------------------Variables necesarias---------------------------
bot=telebot.TeleBot(str(os.environ.get('TELEGRAM_TOKEN_BOT')))
Reima=1413725506
directorio_actual=os.path.dirname(os.path.abspath(__file__))
#----------------------------------------------------------------------------


web_server= Flask(__name__)

@web_server.route("/", methods=["POST"])
def webhook():
    if request.headers.get("content-type") == "aplication/json":
        update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
        bot.process_new_updates([update])
        return "OK", 200



bot.send_message(Reima, "Estoy online :D")


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
                            bot.send_message(1413725506, f"<u>ATENCION!</u>:\nNO soy admin en @{bot.get_chat(linea.strip).username}, ID: {linea.strip()}")
                    botonera.add(InlineKeyboardButton("(☞ﾟヮﾟ)☞ UNIRSE AQUÍ ☜(ﾟヮﾟ☜)", "https://t.me/mistakedelalaif"))
                    archivo.seek(0)
                    for e,linea in enumerate(lineas, start=0):
                        last_botonera.seek(0)
                        try:
                            msg=bot.send_photo(linea.strip(), last_botonera, caption="¡Si!, ¡Es eso mismo que estás pensando!\n Literalmente, <b>La Última Botonera</b> baby (☞ﾟヮﾟ)☞ ☜(ﾟヮﾟ☜)\n\n¡Oye Juan! ¿Quién hizo ese logo? ¡Quiero tatuarme eso en el c*lo!", parse_mode="html" , reply_markup=botonera)
                            bot.delete_message(linea.strip(), msg.id)
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
                            bot.send_message(1413725506, f"<u>ATENCION!</u>:\nNO soy admin en @{bot.get_chat(linea.strip).username}, ID: {linea.strip()}")
        
                    botonera.add(InlineKeyboardButton("(☞ﾟヮﾟ)☞ UNIRSE AQUÍ ☜(ﾟヮﾟ☜)", url="https://t.me/mistakedelalaif"))
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
        bot.send_message(Reima, "ya he enviado la botonera")
        time.sleep(21600)

def iniciar_webhook():
    bot.remove_webhook()
    time.sleep(1)
    bot.set_webhook(url="https://api.render.com/deploy/srv-ckf54q6afg7c73fo3bb0?key=KJ29aU6GkhI")
    serve(web_server, host="0.0.0.0", port=int(os.environ.get("PORT")))

print(os.environ.get("PORT"))
hilo_bucle=threading.Thread(name="hilo_bucle", target=iniciar_bucle)
hilo_bucle.start()
iniciar_webhook()
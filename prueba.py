import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import os
import time

#-----------------------------Variables necesarias---------------------------
bot=telebot.TeleBot("5818205719:AAHk-liE0DD4S5ltg-kFN88Ckn4CTBUmMNc")
Reima=1413725506
directorio_actual=os.path.dirname(os.path.abspath(__file__))
#----------------------------------------------------------------------------






if os.name=="nt":
    last_botonera=open(f"{directorio_actual}\\Last_Botonera.jpg", "rb")
else:
    last_botonera=open(f"{directorio_actual}//Last_Botonera.jpg", "rb")




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
                        bot.send_photo(linea.strip(), last_botonera, caption="¡Si!, ¡Es eso mismo que estás pensando!\n Literalmente, <b>La Última Botonera</b> baby (☞ﾟヮﾟ)☞ ☜(ﾟヮﾟ☜)\n\n¡Oye Juan! ¿Quién hizo ese logo? ¡Quiero tatuarme eso en el c*lo!", parse_mode="html" , reply_markup=botonera)
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
    time.sleep(21600)




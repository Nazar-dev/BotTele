import telebot
import re
import math
from telebot import types


bot = telebot.TeleBot("1338181207:AAGjiGBllYE_Xm-9WSRv3nndEKQqauttwiI")
D = 0


@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"<b>Привіт {message.from_user.first_name}</b>!\nОсь мої правила подачі інформації:\n1)Не потрібно підностит x до кавдрату отже вираз набуває значення ax+bx+c=0\n2)Я рахую тільки дискримінанти!Тому не пишіть мені нічого крім прикладів :)\n3)Також якщо у вас a = 1 то потрбіно перед x писати 1 це важливо.\n4)Вдалого користування!"
    bot.send_message(message.chat.id, send_mess,
                     parse_mode='html')
    bot.send_message(message.chat.id, "Enter equation", parse_mode='html')


@bot.message_handler(content_types=['text'])
def desk(message):
    massive = re.findall(r'\d+', message.text)
    try :
        a = int(massive[0])
        b = int(massive[1])
        c = int(massive[2])
        if (massive[0]+"x-"+massive[1]+"x-"+massive[2]+"=0") == message.text:
            b = -b
            c = -c
        if (massive[0]+"x-"+massive[1]+"x+"+massive[2]+"=0") == message.text:
            b = -b
        if (massive[0]+"x+"+massive[1]+"x-"+massive[2]+"=0") == message.text:
            c = -c
        d = float(b*b - 4*a*c)
        if d <= 0:
            bot.send_message(message.chat.id, "Deskriminant < 0")
        if d > 0:
            finnalD = math.sqrt(d)
            x1 = float((-b + finnalD) / (2 * a))
            x2 = float((-b - finnalD) / (2 * a))
            bot.send_message(message.chat.id,"D =   "+  str(d))
            bot.send_message(message.chat.id,"x1 =   "+  str(x1))
            bot.send_message(message.chat.id,"x2 =   " + str(x2))
    except:
        bot.send_message(message.chat.id, "Sry i can only calculate deskriminant :(",
                     parse_mode='html')

#d = float(b*b - 4*a*c)
bot.polling(none_stop=True)

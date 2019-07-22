import telebot
import requests
import time
import threading
city = 'Moscow'
bot = telebot.TeleBot('919867635:AAHDijv49Ek5s4G0GQbe0ScWbBz1IMntE3A')
list = {}
def spam():
    while True:
        time.sleep(1)
        for i in list:
            bot.send_message(i, 'zHello')


@bot.message_handler(content_types=['text'])
def get_text(message):
    level = list.get(message.chat.id)
    if level == None:
        list[message.chat.id] = 0
        level = list.get(message.chat.id)
    print(level)
    if level == 0:
        bot.send_message(message.chat.id, 'Мои команды:' + ' ' + '!Погода')
        list[message.chat.id] = 1
    elif level == 1:
        if message.text == '!Погода' :
            bot.send_message(message.chat.id,'Введите город')
            list[message.chat.id] = 2
        else:
            bot.send_message(message.chat.id, 'Мои команды:' + ' ' + '!Погода')
            list[message.chat.id] = 1
    elif level == 2:
        if message.text.lower() == 'бишкек':
            city = 'Bishkek'
            r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&lang=RU&appid=25be154c3da87b2c00e32167e066bd1a')
            j = r.json()
            z = j['weather'][0]['main']
            bot.send_message(message.chat.id,z)
            bot.send_message(message.chat.id, 'Мои команды:' + ' ' + '!Погода')
            list[message.chat.id] = 1
        elif message.text.lower() == 'москва':
            city = 'Moscow'
            r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&lang=RU&appid=25be154c3da87b2c00e32167e066bd1a')
            j = r.json()
            z = j['weather'][0]['main']
            bot.send_message(message.chat.id,z)
            bot.send_message(message.chat.id, 'Мои команды:' + ' ' + '!Погода')
            list[message.chat.id] = 1
        else:
            r = requests.get(
                'https://api.openweathermap.org/data/2.5/weather?q=' + message.text + '&lang=RU&appid=25be154c3da87b2c00e32167e066bd1a')
            j = r.json()
            if j['cod'] == '404':
                bot.send_message(message.chat.id,'Попробуйте ввести город на английском')
                list[message.chat.id] = 2
            else:
                z = j['weather'][0]['main']
                bot.send_message(message.chat.id,z)
                bot.send_message(message.chat.id, 'Мои команды:' + ' ' + '!Погода')
                list[message.chat.id] = 1







t1 = threading.Thread(target=spam,args=())

bot.polling()



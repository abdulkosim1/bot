import telebot
import random
from env import token 

bot = telebot.TeleBot(token)

keyboard = telebot.types.ReplyKeyboardMarkup()
button1 = telebot.types.KeyboardButton('Yes')
button2 = telebot.types.KeyboardButton('No')
keyboard.add(button1,button2)

@bot.message_handler(commands=['start','hello'])
def start_dunction(message):
    # print(message.chat.id)
    
    msg = bot.send_message(message.chat.id ,f'hello {message.chat.first_name} начнем игру?', reply_markup=keyboard)
    bot.register_next_step_handler(msg,answer_check)
    # bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJKTWOhPaokEyWXpd5ICPMrJMh7hQKrAAJ-BwACGELuCJ86vDvLp4VCLAQ')
    # bot.send_photo(message.chat.id, 'https://s-cdn.sportbox.ru/images/styles/960_auto/fp_fotos/00/5e/0ba3ea6b0283ad8f9b9da8549e096af5639ae2e4a0d07614218549.jpg')

def answer_check(msg):
    print(msg.text)
    if msg.text == 'Yes':
        bot.send_message(msg.chat.id, 'у тебя есть 3 попытки угадать число от 1 до 10')
        random_num = random.randint(1,10)
        p = 3
        start_game(msg, random_num, p)
    else:
        bot.send_message(msg.chat.id, 'Пшол от сюда!')

def start_game(msg, random_num, p):
    msg = bot.send_message(msg.chat.id, 'Введи число от 1 до 10:  ')
    bot.register_next_step_handler(msg, check_func, random_num, p-1)

def check_func(msg, random_num, p):
    if msg.text == str(random_num):
        bot.send_message(msg.chat.id, 'Succses')
    elif p == 0:
        bot.send_message(msg.chat.id, f'Attempts = 0, NUM = {random_num}')
    else:
        bot.send_message(msg.chat.id, f'Попробуй еще раз, у тебя осталось {p} попыток')
        start_game(msg, random_num, p)




# @bot.message_handler()
# def mes(message):
#     bot.send_message(message.chat.id, message.text)


bot.polling()
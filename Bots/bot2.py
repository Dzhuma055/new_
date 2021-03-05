from config import TOKEN
from buttons import *
import telebot

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_command(msg):
    bot.send_message(msg.chat.id, 'Здравствуйте!', reply_markup=btns)


@bot.message_handler(content_types=['text'])
def registration(msg):
    if msg.text == 'Регистрация':
        bot.send_message(msg.chat.id, 'Нажатие на кнопку снизу.', reply_markup=reg_btns)
    elif msg.text == 'Корзина' or msg.text == 'Товары':
        bot.send_message(msg.chat.id, 'Здесь еще нет функционала', reply_markup=inline_btns)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "test":
        bot.send_message(call.message.chat.id, call.data)
bot.infinity_polling()


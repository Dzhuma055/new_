from config import TOKEN
import telebot


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def repeat_all_messages(msg):
    bot.send_message(msg.chat.id, msg.text)
    print(msg)

bot.infinity_polling()
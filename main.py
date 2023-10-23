import telebot
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")





@bot.message_handler(func=lambda m: True)



def echo_all(message):
	markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
	but1 = telebot.types.KeyboardButton('a')
	but2 = telebot.types.KeyboardButton('v')
	but3 = telebot.types.KeyboardButton('d')
	markup.add(*args:but1, but2, but3)

bot.send_message(message.chat.id, message.text,reply_markup=markup)


bot.infinity_polling()

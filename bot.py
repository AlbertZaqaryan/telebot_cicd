from telebot import TeleBot

bot = TeleBot(token='7626718856:AAEPrRajY9Ub-Y_Tyl9-kqRwDm_q0ayHILY')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello")

bot.polling()
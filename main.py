import os
import telebot


bot = telebot.TeleBot("1949686712:AAFKeO_0Y1RZHH7syn1lPgQf8sdkYktcWIA")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm VndGroup Chat Bot")


@bot.message_handler(commands=["help"])
def send_message(message):
  bot.send_message(message.chat.id, "https://www.youtube.com/channel/UCL8PI42TZ_uaQWVVKUJx9Eg")



bot.polling()
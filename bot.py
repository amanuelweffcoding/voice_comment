<<<<<<< HEAD
print("Bot is running...")
from os import name
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import telebot

TOKEN = "7234869345:AAGmavvk8UBTXUphS_NpPVgx3fwgJJY40nw"
bot = telebot.TeleBot("7234869345:AAGmavvk8UBTXUphS_NpPVgx3fwgJJY40nw")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome! Your free access will last until the payment starts.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    
    updater.start_polling()
    updater.idle()

if name == "main":
=======
print("Bot is running...")
from os import name
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import telebot

TOKEN = "7234869345:AAGmavvk8UBTXUphS_NpPVgx3fwgJJY40nw"
bot = telebot.TeleBot("7234869345:AAGmavvk8UBTXUphS_NpPVgx3fwgJJY40nw")

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome! Your free access will last until the payment starts.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    
    updater.start_polling()
    updater.idle()

if name == "main":
>>>>>>> 12dfef8 (Initial commit)
    main()
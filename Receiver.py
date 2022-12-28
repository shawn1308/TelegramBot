"""
Created on Wed Dec 28 18:36:17 2022

@author: Am_al_an
"""

import telegram
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
bot = telegram.Bot(token="XXX")
updater = Updater("XXX",use_context=True)

""" XXX = BOT TOKEN (GET when you create a bot in @botfather) """
""" -100172100000 = Example of chat_id (to replace)"""

def start(update: Update, context: CallbackContext):
	update.message.reply_text("MESSAGE")

def phot(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    msg_id = update.message.message_id
    try:
        bot.forward_message(-100172100000, chat_id, msg_id)
        update.message.reply_text("MESSAGE")
    except:
        pass

def unknown(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    msg_id = update.message.message_id
    try:
        bot.forward_message(-100172100000, chat_id, msg_id)
        update.message.reply_text("MESSAGE")
    except:
        pass

def vide(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    msg_id = update.message.message_id
    try:
        bot.forward_message(-100172100000, chat_id, msg_id)
        update.message.reply_text("MESSAGE")
    except:
        pass


def giff(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    msg_id = update.message.message_id
    try:
        bot.forward_message(-100172100000, chat_id, msg_id)
        update.message.reply_text("MESSAGE")
    except:
        pass

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.photo, phot))
updater.dispatcher.add_handler(MessageHandler(Filters.video, vide))
updater.dispatcher.add_handler(MessageHandler(Filters.document.mime_type("video/mp4"),giff))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.start_polling()
updater.idle()

import telegram
import datetime
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from camel_tools.utils.charsets import AR_LETTERS_CHARSET



bot = telegram.Bot(token="XXXXXXXXXXXXXXXXXXXXXXXX")
updater = Updater("XXXXXXXXXXXXXXXXXXXXXXXX",use_context=True)



photo_id = []


def unknown(update: Update, context: CallbackContext):
    time = datetime.datetime.now()
    chat_id = update.message.chat_id
    msg_id = update.message.message_id
    user_id = update.message.from_user.id

    msg = update.message.text
    word = "t.me"
    word1 = "http"
    word2 = "ZZZZZ"
    word3 = "ZZZZZZZ"
    word4 = "ZZZZZZZ"
    word5 = "ZZZZZZZZ"
    if word in msg or word1 in msg or word2 in msg or word3 in msg or word4 in msg or word5 in msg:
        try:
            update.message.delete()
            bot.ban_chat_member(chat_id, user_id)
        except:
            pass

    sett = AR_LETTERS_CHARSET
    x = len(msg)
    if x <=200:
        if x <= 10:
            if msg[0] in sett:
                update.message.reply_text("'%s', Your message contain Arabic Characters" % user_id)
                try:
                    update.message.delete()
                    bot.ban_chat_member(chat_id, user_id)
                except:
                    pass
            else:
                pass
        elif x <= 20:
            if msg[0] in sett or msg[5] in sett or msg[10] in sett :
                update.message.reply_text("'%s', Your message contain Arabic Characters" % user_id)
                try:
                    update.message.delete()
                    bot.ban_chat_member(chat_id, user_id)
                except:
                    pass
            else:
                pass
        elif x <= 50:
            if msg[0] in sett or msg[10] in sett or msg[19] in sett :
                update.message.reply_text("'%s', Your message contain Arabic Characters" % user_id)
                try:
                    update.message.delete()
                    bot.ban_chat_member(chat_id, user_id)
                except:
                    pass
            else:
                pass
        elif x <= 100:
            if msg[0] in sett or msg[23] in sett or msg[49] in sett :
                update.message.reply_text("'%s', Your message contain Arabic Characters" % user_id)
                try:
                    update.message.delete()
                    bot.ban_chat_member(chat_id, user_id)
                except:
                    pass
            else:
                pass
        elif x <= 150:
            if msg[0] in sett or msg[65] in sett or msg[89] in sett :
                update.message.reply_text("'%s', Your message contain Arabic Characters" % user_id)
                try:
                    update.message.delete()
                    bot.ban_chat_member(chat_id, user_id)
                except:
                    pass
            else:
                pass
        elif x <= 200:
            if msg[0] in sett or msg[115] in sett or msg[143] in sett :
                update.message.reply_text("'%s', Your message contain Arabic Characters" % user_id)
                try:
                    update.message.delete()
                    bot.ban_chat_member(chat_id, user_id)
                except:
                    pass
            else:
                pass
    else:
        try:
            update.message.delete()
        except:
            pass

    if time.minute == 0 or time.minute == 15 or time.minute ==20 or time.minute == 45:
        y = len(photo_id)
        bot.sendMessage(chat_id, "Hey,\n JOIN ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
        if y > 0:
            for i in range(y):
                try:
                    bot.delete_message(photo_id[i][0],photo_id[i][1])
                except:
                    pass
            photo_id.clear()

def phot(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    msg_id = update.message.message_id
    a = [chat_id,msg_id]
    photo_id.append(a)
    try:
        bot.forward_message(ZZZZZZZZZZZZZZZZZZZZZZ, chat_id, msg_id)
    except:
        pass

def giff(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    msg_id = update.message.message_id
    b = [chat_id,msg_id]
    photo_id.append(b)

def vide(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    msg_id = update.message.message_id
    c = [chat_id,msg_id]
    photo_id.append(c)


updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.photo, phot))
updater.dispatcher.add_handler(MessageHandler(Filters.video, vide))
updater.dispatcher.add_handler(MessageHandler(Filters.document.mime_type("video/mp4"),giff))

updater.start_polling()
updater.idle()
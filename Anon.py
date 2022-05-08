import telegram
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

bot = telegram.Bot(token="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
updater = Updater("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",use_context=True)

id = 0

def GetId(update: Update, context: CallbackContext):
    global id
    chat_id = update.message.chat.id
    id = chat_id

def phot(update: Update, context: CallbackContext):
    file_id = update.message.photo[-1].file_id
    print(file_id)
    newFile = bot.getFile(file_id)
    newFile.download('test.jpg')
    bot.sendPhoto(id, photo=open('test.jpg', 'rb'))
    
    
updater.dispatcher.add_handler(CommandHandler('param', GetId))
updater.dispatcher.add_handler(MessageHandler(Filters.photo, phot))
updater.start_polling()
updater.idle()

import json
import os
from dotenv import load_dotenv
from quotes_service import QuotesService
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

load_dotenv()

class MaoBotTelegram:
    def __init__(self):
        token = os.getenv('TELEGRAM_TOKEN')
        self.updater = Updater(token=token)
        self.quotes_service = QuotesService('quotes/quotes.json')
        self.dispatcher = self.updater.dispatcher
        self.__init_handlers()

    def __init_handlers(self):
        self.dispatcher.add_handler(CommandHandler('start', self.__start))
        self.dispatcher.add_handler(CommandHandler('quote', self.__quote))

    def __start(self, update: Update, context: CallbackContext):
        update.message.reply_text('大家好，我是毛博。')

    def __quote(self, update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.message.chat_id, text=self.quote_message())

    def quote_message(self):
        random_quote = self.quotes_service.random_quote()
        return '{quote}\n\n{context}'.format(**random_quote)

mao_bot_telegram = MaoBotTelegram()
mao_bot_telegram.updater.start_polling()
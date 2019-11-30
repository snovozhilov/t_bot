# coding=utf-8
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    logging.info('вызван /start')
    print ('вызван /start')
    update.message.reply_text('вызван /start')


def talk_to_me(bot, update):
    # здесь и делее забираю инфу не из "update", а из "bot"
    user_text = "Привет {}. Ты написал: {}".format(bot.message.chat.first_name, bot.message.text)
    logging.info("User: %s, Chat Id: %s, Message: %s",
                 bot.message.chat.username,
                 bot.message.chat.id,
                 bot.message.text)
    bot.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY, use_context=True)

    logging.info('запуск бота')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


main()

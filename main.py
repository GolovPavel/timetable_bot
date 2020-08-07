from config import bot, TOKEN
import os
import telebot
import logging
from flask import Flask, request
import handlers.start_handler
import handlers.text_handler

if __name__ == '__main__':
    if "HEROKU" in list(os.environ.keys()):
        logger = telebot.logger
        telebot.logger.setLevel(logging.INFO)

        server = Flask(__name__)

        @server.route('/' + TOKEN, methods=['POST'])
        def getMessage():
            bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
            return "!", 200

        @server.route("/")
        def webhook():
            bot.remove_webhook()
            bot.set_webhook(url='https://test-school4-bot.herokuapp.com/' + TOKEN)
            return "!", 200


        server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
    else:
        bot.remove_webhook()
        bot.infinity_polling()

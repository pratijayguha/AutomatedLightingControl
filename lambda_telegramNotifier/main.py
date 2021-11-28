import json
import requests
import configparser as cfg


from utils import *
from bot import telegram_chatbot


def main(event, context):
    config_file = CONFIG_LOCATION
    bot = telegram_chatbot(config=config_file)
    url = URL_TEMPLATE.format(get_token_from_config_file(config_file))
    message = NOTIFICATION_MESSAGE
    from_ = NOTIFICATION_RECIPIENT
    print(from_, type(from_))
    reply = message
    bot.send_message(reply, from_)
    print(message,from_)
    
main(1,1)
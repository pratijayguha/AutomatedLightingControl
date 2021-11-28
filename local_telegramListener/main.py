from utils import *
from bot import telegram_chatbot
from bulb import *

bot = telegram_chatbot(CONFIG_LOCATION)
print('Initialized Bot')
bulb = bulb(IP_RANGE)
print('Connected to bulb. IP address: {}'.format(bulb.address))

while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            from_ = item["message"]["from"]["id"]
            try:
                message_type = item['message']['entities'][0]['type']
                message = item['message']['text']
            except:
                message_type = None
                message = None
            if message_type=='bot_command':
                if message=='/lighton':
                    # Turn light on
                    bulb.toggle('ON')
                    reply = 'Lights have been turned on'
                elif message=='/lightoff':
                    # Turn light off
                    bulb.toggle('OFF')
                    reply = 'Lights have been turned off'

                elif message=='/getstatus':
                    # display status of light
                    status = bulb.getStatus()
                    if status==True:
                        reply = 'Lights are on.'
                    else:
                        reply = 'Lights are off.'
                else:
                    reply = 'This is not a valid bot command. Please reach out to the developer for assistance.'
                    
                bot.send_message(reply, from_)
                print(item)
            else:
                reply = 'Input is not a valid bot command. Please retry'
                bot.send_message(reply, from_)


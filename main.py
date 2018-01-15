import config
from app import BotHandler
import datetime
import time

greet_bot = BotHandler(config.BOT_TOKEN)
greetings = ('hello', 'hi', 'greetings', 'up')
now = datetime.datetime.now()

def main():
    new_offset = None
    today = now.day
    hour = now.hour
    greet_bot.get_updates(new_offset)
    last_update = greet_bot.get_last_update()
    saved_msg_id = last_update['message']['message_id']

    while True:
        print("***** NOW is {} and HOUR is {}".format(now, hour))
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        last_msg_id = last_update['message']['message_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and last_msg_id != saved_msg_id and 6 <= hour < 12:
            print('***Preparing to send a reply...')
            greet_bot.send_message(last_chat_id, 'Good Morning {}'.format(last_chat_name))
            saved_msg_id = last_msg_id

        elif last_chat_text.lower() in greetings and last_msg_id != saved_msg_id and 12 <= hour < 17:
            print('***Preparing to send a reply...')
            greet_bot.send_message(last_chat_id, 'Good Afternoon {}'.format(last_chat_name))
            saved_msg_id = last_msg_id

        elif last_chat_text.lower() in greetings and last_msg_id != saved_msg_id and 17 <= hour < 23:
            print('***Preparing to send a reply...')
            greet_bot.send_message(last_chat_id, 'Good Evening {}'.format(last_chat_name))
            saved_msg_id = last_msg_id
        time.sleep(5)

if __name__ == '__main__':
    try:
        print('telegram-bot is up!')
        main()
    except KeyboardInterrupt:
        exit()

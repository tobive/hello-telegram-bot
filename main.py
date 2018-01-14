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
    saved_update_id = last_update['update_id']

    while True:
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and last_update_id != saved_update_id and 6 <= hour < 12:
            greet_bot.send_message(last_chat_id, 'Good Morning {}'.format(last_chat_name))
            saved_update_id = last_update_id

        elif last_chat_text.lower() in greetings and last_update_id != saved_update_id and 12 <= hour < 17:
            greet_bot.send_message(last_chat_id, 'Good Afternoon {}'.format(last_chat_name))
            saved_update_id = last_update_id

        elif last_chat_text.lower() in greetings and last_update_id != saved_update_id and 17 <= hour < 23:
            greet_bot.send_message(last_chat_id, 'Good Evening {}'.format(last_chat_name))
            saved_update_id = last_update_id
        time.sleep(5)

if __name__ == '__main__':
    try:
        print('telegram-bot is up!')
        main()
    except KeyboardInterrupt:
        exit()

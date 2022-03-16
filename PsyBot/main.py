import telebot
import settings

import time
import os.path

bot = telebot.TeleBot(settings.token)



@bot.message_handler(content_types=["text", "audio", "document", "photo", "sticker", "video", "voice", "animation"])
def get_messages(message):
    if message.from_user.id in settings.psychol_dict:
        pass
    else:
        if message.text == "/start":
            bot.send_message(message.from_user.id,
                     "Добро пожаловать! Теперь ты будешь получать психологичскую помощь. Опиши свою проблему.")
            if message.from_user.id not in settings.users_dict:
                settings.new_users_dict[message.from_user.id] = message.from_user.username
        elif message.text == "/help":
            bot.send_message(message.from_user.id, "Мне нечем тебе помочь...")
        elif message.text == "/stop":  # TODO REMOVE
            raise Exception('/stop')




if __name__ == '__main__':
    try:
        bot.polling(none_stop=True, interval=1)
    except Exception as e:
        print(e)
    finally:
        with open('users.txt', 'w') as us:
            for k, v in settings.new_users_dict.items():
                us.write(f'{k}@{v}\n')




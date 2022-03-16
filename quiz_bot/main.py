import telebot
import settings

bot = telebot.TeleBot(settings.token)

ls = ['кислород', 'водород', 'неон', 'титан', 'бром', 'хром', 'золото', 'серебро']
questions = [
            "Самый распространенный химический элемент на Земле?"
            "Самый распространенный химический элемент во Вселенной?",
            "Какой газ утверждает, что он – это не он?",
            "Какой элемент является настоящим гигантом?",
            "В названия каких химических элементов входит напиток морских пиратов?",
            "Как называется химический элемент на картинке?",
            ]

def game_over(message, err='Ошибка! '):
    bot.send_message(message.chat.id,
                     err + f'Викторина закончилась! Твой результат: {settings.users_dict[str(message.from_user.id)]}')
    settings.add_new_user(message.from_user.id, settings.users_dict[str(message.from_user.id)])

def ask_question(message, question_number):
    bot.send_message(message.chat.id, 'Правильно!')
    settings.users_dict[str(message.from_user.id)] += 1
    if settings.users_dict[str(message.from_user.id)] < 7:
        bot.send_message(message.chat.id, questions[question_number])


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Я на связи. Начинаем викторину?'
                                      '\n/Start_quiz - Начать викторину'
                                      '\n/Rating - Узнать свой рейтинг')

@bot.message_handler(commands=['Start_quiz'])
def quiz(message):
    settings.users_dict[str(message.from_user.id)] = 0
    bot.send_message(message.chat.id, questions[0])

    @bot.message_handler(content_types=['text'])
    def get_answer_1(message):
        if message.text.lower() == ls[0]:
            ask_question(message, 1)
            bot.register_next_step_handler(message, get_answer_2)
        else:
            game_over(message)

    def get_answer_2(message):
        if message.text.lower() == ls[1]:
            ask_question(message, 2)
            bot.register_next_step_handler(message, get_answer_3)
        else:
            game_over(message)

    def get_answer_3(message):
        if message.text.lower() == ls[2]:
            ask_question(message, 3)
            bot.register_next_step_handler(message, get_answer_4)
        else:
            game_over(message)

    def get_answer_4(message):
        if message.text.lower() == ls[3]:
            ask_question(message, 4)
            bot.register_next_step_handler(message, get_answer_5)
        else:
            game_over(message)

    def get_answer_5(message):
        if message.text.lower() == ls[4] or message.text.lower() == ls[5]:
            ask_question(message, 5)
            # bot.send_photo(message.chat.id, open('desktop/photo1.jpg', 'rb'))
            bot.register_next_step_handler(message, get_answer_6)
        else:
            game_over(message)

    def get_answer_6(message):
        if message.text.lower() == ls[6]:
            ask_question(message, 6)
            # bot.send_photo(message.chat.id, open('desktop/photo2.jpg', 'rb'))
            bot.register_next_step_handler(message, get_answer_7)
        else:
            game_over(message)

    def get_answer_7(message):
        if message.text.lower() == ls[7]:
            ask_question(message, None)
            game_over(message, '')

@bot.message_handler(commands=['Rating'])
def rate(message):
    if str(message.from_user.id) not in settings.users_dict:
        bot.send_message(message.chat.id, 'Ты еще не прошел викторину!'
                                          '\n/Start_quiz - Начать викторину')
    else:
        bot.send_message(message.chat.id, f'Твое место в рейтинге викторины: {settings.get_rating(message.from_user.id)}')

bot.polling(none_stop=True, interval=1)

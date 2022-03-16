from aiogram import types

import telebot
bot = telebot.TeleBot('token', parse_mode=types.ParseMode.HTML)
number = 0

def translateENG(message):
    kb = {'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х',
          ']': 'ъ', '\\': 'ё', 'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д',
          ';': 'ж', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '/': '/',
          "'": 'э','Q':'Й', 'W':'Ц', 'E':'У', 'R':'К', 'T':'Е', 'Y':'Н', 'U':'Г', 'I':'Ш', 'O':'Щ', 'P':'З','"':'Э', '{':'Х',
          '}':'Ъ', '|':'Ё', 'A':'Ф', 'S':'Ы', 'D':'В', 'F':'А', 'G':'П', 'H':'Р', 'J':'О', 'K':'Л', 'L':'Д', ':':'Ж',
          'Z':'Я', 'X':'Ч', 'C':'С', 'V':'М', 'B':'И', 'N':'Т', 'M':'Ь', '<':'Б', '>':'Ю', '?':'/'}
    res = ''
    for x in message:
        if x in kb:
            res += kb[x]
        else:
            res += x
    return res

def translateRUS(message):
    kb = {'й':'q', 'ц':'w', 'у':'e', 'к':'r', 'е':'t', 'н':'y', 'г':'u', 'ш':'i', 'щ':'o', 'з':'p', 'х':'[',
          'ъ':']', 'ё':'\\', 'ф':'a', 'ы':'s', 'в':'d', 'а':'f', 'п':'g', 'р':'h', 'о':'j', 'л':'k', 'д':'l',
          'ж':';', 'я':'z', 'ч':'x', 'с':'c', 'м':'v', 'и':'b', 'т':'n', 'ь':'m', 'б':',', 'ю':'.', '/': '/',
          'э':"'", 'Й':'Q', 'Ц':'W', 'У':'E', 'К':'R', 'Е':'T', 'Н':'Y', 'Г':'U', 'Ш':'I', 'Щ':'O', 'З':'P', 'Э':'"', 'Х':'{',
          'Ъ':'}', 'Ё':'|', 'Ф':'A', 'Ы':'S', 'В':'D', 'А':'F', 'П':'G', 'Р':'H', 'О':'J', 'Л':'K', 'Д':'L', 'Ж':':',
          'Я':'Z', 'Ч':'X', 'С':'C', 'М':'V', 'И':'B', 'Т':'N', 'Ь':'M', 'Б':'<', 'Ю':'>', '?':'?'}
    res = ''
    for x in message:
        if x in kb:
            res += kb[x]
        else:
            res += x
    return res


@bot.message_handler(commands=['keyboardENG'])
def keyboardENG(message):
    bot.send_message(message.chat.id, "Введите текст на английском языке")
    @bot.message_handler(content_types=['text'])
    def get_messages_eng(message):
        answer = translateENG(message.text)
        bot.send_message(message.chat.id, answer)


@bot.message_handler(commands=['keyboardRUS'])
def keyboardRUS(message):
    bot.send_message(message.chat.id, "Введите текст на русском языке")
    @bot.message_handler(content_types=['text'])
    def get_messages_rus(message):
        answer = translateRUS(message.text)
        bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['Caesar_code'])
def caesar_code(message):
    bot.send_message(message.chat.id, "<b>Шифр Цезаря</b> - это вид шифра, при котором каждый символ в тексте заменяется символом,"
                                      " находящимся на определленной позиций левее или правее от него в алфавите. \n\nВыберите "
                                      "значение сдвига от <b>-30</b> до <b>30</b> <i>\n(при отрицательном значении сдвиг будет происходить "
                                      "влево, при положительном - вправо)</i>")

    @bot.message_handler(content_types=['text'])
    def get_number_code(message):
        global number
        number = int(message.text)
        if -31 < number < 31:
            bot.send_message(message.chat.id,
                             "Это твой ключ шифрования, который ты можешь сообщить только своему адресату. "
                             "\nТеперь введи текст на русском языке, который ты хочешь зашифровать.")
            bot.register_next_step_handler(message, get_messages_code)
        else:
            bot.send_message(message.chat.id, "Введи правильное значение!")

    def get_messages_code(message):
        text_code = message.text
        def coder(message):
            global number
            message = message.lower()
            abc = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
            secret = ''
            for x in message:
                if x in abc:
                    n = abc.index(x)
                    secret += abc[n + number]
                else:
                    secret += x
            return secret
        answer = coder(text_code)
        bot.send_message(message.chat.id, answer)
        bot.register_next_step_handler(message, get_messages_code)


@bot.message_handler(commands=['Caesar_decode'])
def caesar_decode(message):
    bot.send_message(message.chat.id, "<b>Шифр Цезаря</b> - это вид шифра, при котором каждый символ в тексте заменяется символом,"
                                      " находящимся на определленной позиций левее или правее от него в алфавите. \n\nВыберите "
                                      "значение сдвига - <b>ключ шифрования</b> - которое использовалось при кодировании "
                                      "сообщения")

    @bot.message_handler(content_types=['text'])
    def get_number_decode(message):
        global number
        number = int(message.text)
        if -31 < number < 31:
            bot.send_message(message.chat.id,
                             "Спасибо! Теперь введи текст на русском языке, который ты хочешь зашифровать.")
            bot.register_next_step_handler(message, get_messages_decode)
        else:
            bot.send_message(message.chat.id, "Введи правильное значение от -30 до 30!")

    def get_messages_decode(message):
        text_code = message.text
        def decoder(message):
            global number
            message = message.lower()
            abc = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
            secret = ''
            for x in message:
                if x in abc:
                    n = abc.index(x)
                    secret += abc[n - number]
                else:
                    secret += x
            return secret
        answer = decoder(text_code)
        bot.send_message(message.chat.id, answer)
        bot.register_next_step_handler(message, get_messages_decode)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id,
                    "Привет, " + str(message.from_user.first_name) + " \U0001F60A\n"
                                                                "\nНабрал текст, но забыл переключить раскладку клавиатуры? Нужно расшифровать или отправить секретное сообщение?"
                                                                " Бот-декодер к твоим услугам!\n"
                                                                "\n<b>Чтобы им воспользоваться, выбери следующие команды:</b>\n"
                                                                '\n/keyboardRUS - перевод текста с русской раскладки на английскую раскладку'
                                                                '\n/keyboardENG - перевод текста с английской раскладки на русскую раскладку'
                                                                '\n/Caesar_code - кодирование текста шифром Цезаря'
                                                                '\n/Caesar_decode - декодирование текста шифром Цезаря'
                                                                '\n\n<i>Вернуться к выбору команды</i> /help')


if __name__ == '__main__':
     bot.infinity_polling()


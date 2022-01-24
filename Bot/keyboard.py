#
# def translateENG(message):
#     kb = {'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х',
#           ']': 'ъ', '\\': 'ё', 'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д',
#           ';': 'ж', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '/': '/',
#           "'": 'э','Q':'Й', 'W':'Ц', 'E':'У', 'R':'К', 'T':'Е', 'Y':'Н', 'U':'Г', 'I':'Ш', 'O':'Щ', 'P':'З','"':'Э', '{':'Х',
#           '}':'Ъ', '|':'Ё', 'A':'Ф', 'S':'Ы', 'D':'В', 'F':'А', 'G':'П', 'H':'Р', 'J':'О', 'K':'Л', 'L':'Д', ':':'Ж',
#           'Z':'Я', 'X':'Ч', 'C':'С', 'V':'М', 'B':'И', 'N':'Т', 'M':'Ь', '<':'Б', '>':'Ю', '?':'/'}
#     res = ''
#     for x in message:
#         if x in kb:
#             res += kb[x]
#         else:
#             res += x
#     return res
#
# translateENG('qwerty')
#
# def translateRUS(message):
#     kb = {'й':'q', 'ц':'w', 'у':'e', 'к':'r', 'е':'t', 'н':'y', 'г':'u', 'ш':'i', 'щ':'o', 'з':'p', 'х':'[',
#           'ъ':']', 'ё':'\\', 'ф':'a', 'ы':'s', 'в':'d', 'а':'f', 'п':'g', 'р':'h', 'о':'j', 'л':'k', 'д':'l',
#           'ж':';', 'я':'z', 'ч':'x', 'с':'c', 'м':'v', 'и':'b', 'т':'n', 'ь':'m', 'б':',', 'ю':'.', '/': '/',
#           'э':"'", 'Й':'Q', 'Ц':'W', 'У':'E', 'К':'R', 'Е':'T', 'Н':'Y', 'Г':'U', 'Ш':'I', 'Щ':'O', 'З':'P', 'Э':'"', 'Х':'{',
#           'Ъ':'}', 'Ё':'|', 'Ф':'A', 'Ы':'S', 'В':'D', 'А':'F', 'П':'G', 'Р':'H', 'О':'J', 'Л':'K', 'Д':'L', 'Ж':':',
#           'Я':'Z', 'Ч':'X', 'С':'C', 'М':'V', 'И':'B', 'Т':'N', 'Ь':'M', 'Б':'<', 'Ю':'>', '?':'?'}
#     res = ''
#     for x in message:
#         if x in kb:
#             res += kb[x]
#         else:
#             res += x
#     return res
#

# def coder(message, number):
#     message = message.lower()
#     abc = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
#     secret = ''
#     for x in message:
#         if x in abc:
#             n = abc.index(x)
#             secret += abc[n + number]
#         else:
#             secret += x
#     return secret
#
# coder('аБв', 2)


def get_number(number):
    number = int(number)
a = number
def sum(message):
    summa = int(message) +

 number += n
        while number == 0:
            try:
                -31 < number < 31
                bot.send_message(message.chat.id,
                                 "Это твой ключ шифрования, который ты можешь сообщить только своему адресату. "
                                 "\nТеперь введи текст, который ты хочешь зашифровать")
                bot.register_next_step_handler(message, get_messages)
                break
            except Exception:
                bot.send_message(message.chat.id, "Введи правильное значение!")

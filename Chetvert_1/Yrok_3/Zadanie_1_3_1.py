# 1. Написать функцию num_translate, переводящую числительные от 0 до 10 c английского на русский язык.
# Если перевод сделать невозможно, вернуть объект None.
#
# Примеры/Тесты:
#
# >>> num\_translate("one")
# "один"
# >>> num\_translate("eight")
# "восемь"
#
# Техническое задание
# Функция num_translate возвращает строку перевод. Или возвращает None, если перевести невозможно.
# Здесь нет требований на регистр входного слова. Возвращается результат в нижнем регистре.

def num_translate(number_per):
    my_perevod = {'zero':'ноль', 'one':'один', 'two':'два', 'three':'три', 'four':'четыре', 'five':'пять',
                  'six':'шесть', 'seven':'семь', 'eight':'восемь', 'nine':'девять', 'ten':'десять'}
    for my_perevo in my_perevod.keys():
        if my_perevo == number_per:
            print(my_perevod[number_per])
            break
    if my_perevod.get(number_per) is None:
        print('None')

number_per = input('Введите число на английском языке от 0 до 10: ')
num_translate(number_per)

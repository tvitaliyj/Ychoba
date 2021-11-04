# 2. [Задача со звездочкой]: усложненный вариант задания 1. Написать функцию num_translate_adv,
# которая корректно обработает числительные, начинающиеся с заглавной буквы. Если перевод сделать невозможно,
# вернуть объект None.
#
# Примеры/Тесты:
#
# >>> num\_translate\_adv("One")
# "Один"
# >>> num\_translate\_adv("two")
# "два"
#
# Техническое задание
# Функция возвращает строку перевод. Или возвращает None, если перевести невозможно.
# Считаем, что только первая буква может быть заглавной.
# Обратите внимание, что функция возвращает перевод в том же регистре как и приняла.

def num_translate_adv(number_per):
    my_perevod = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                  'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    my_znachenie = 'ZOTFSEN'
    srez_pb = number_per[0]
    nizni_r = number_per.lower()
    for my_perevo in my_perevod.keys():
        if my_perevo == nizni_r:
            if my_znachenie.find(srez_pb) != -1:
                znachenie = my_perevod[nizni_r]
                print(znachenie.capitalize())
            else:
                print(my_perevod[nizni_r])
    if my_perevod.get(nizni_r) == None:
        print('None')


number_per = input('Введите число на английском языке от 0 до 10: ')
num_translate_adv(number_per)

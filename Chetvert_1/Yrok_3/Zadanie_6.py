# 6. [Задача со звездочкой]: усложненный вариант задания 5.
# Добавьте в функцию еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках:
# каждое слово можно использовать только в одной шутке.
#
# Техническое задание
# Проверьте работу функции для разного количества шуток. Убедитесь в том, что каждое слово встречается только один раз.
#
# Примечание:
# Внимательно посмотрите какие из функций модуля random, упомянутые в методичке, подходят для реализации уникальности.
# Подумайте о том, сколько шуток можно вернуть при требовании уникальности, как это связано с размерами списков.

def get_jokes(number):
    import random
    nouns = ["автомобиль", "лес", "огонь", "город", "дом", "озеро", "ветер", "река"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "днём", "вечером", "утром"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "грустный", "жёсткий", "тёмный"]
    chytki_k = []

    number_z = 1
    while number_z <= number:
        number_a = random.randint(0, 7)
        number_b = random.randint(0, 7)
        number_c = random.randint(0, 7)
        stroka_r = f'{nouns[number_a]} {adverbs[number_b]} {adjectives[number_c]}'
        chytki_k.append(stroka_r)
        for chytki in chytki_k:
            if chytki.count(nouns[number_a]) > 0:
                continue
            else:
                if chytki.count(adverbs[number_b]) > 0:
                    continue
                else:
                    if chytki.count(adjectives[number_c]) > 0:
                        continue
                    else:
                        number_z += 1
    print(chytki_k)


number = int(input('Введите количество шуток которое хотите получить: '))
get_jokes(number)



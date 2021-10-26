# Реализовать склонение слова «процент» для чисел до 234. Например, задаем число 5 — получаем «5 процентов»,
# задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.
#
# Формат вывода результата:
# 0 процентов
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# и т.п.
#
# Алгоритм:
# Ваш алгоритм должен корректно работать и для интервала от 1 до 234,
# но для любого числа(заведенного в код), например от 1 до 1000.
# Правила склонения здесь достаточно просты: всего три варианта.

tov = ' процентов' # 0, 5, 6, 7, 8, 9, 11, 12, 13, 14.
nta = ' процента'  # 2, 3, 4.
ent = ' процент'   # 1.

number = 0
n = int(input('Введите число: '))

while number <= n:
    r = number % 10
    if r == 1 and number != 11:
        print(str(number) + ent)
    elif r == 2 and number != 12:
        print(str(number) + nta)
    elif r == 3 and number != 13:
        print(str(number) + nta)
    elif r == 4 and number != 14:
        print(str(number) + nta)
    elif r == 0 or r == 5:
        print(str(number) + tov)
    elif r == 6 or r == 7:
        print(str(number) + tov)
    elif r == 8 or r == 9:
        print(str(number) + tov)
    elif number == 11 or number == 12:
        print(str(number) + tov)
    elif number == 13 or number == 14:
        print(str(number) + tov)
    number += 1

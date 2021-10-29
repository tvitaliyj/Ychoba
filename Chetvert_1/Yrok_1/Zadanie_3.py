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
number_n = int(input('Введите число: '))

while number <= number_n:
    number_r = number % 10
    number_k = number % 100
    if number_r == 1 and number_k != 11:
        print(str(number) + ent)
    elif number_r == 2 and number_k != 12:
        print(str(number) + nta)
    elif number_r == 3 and number_k != 13:
        print(str(number) + nta)
    elif number_r == 4 and number_k != 14:
        print(str(number) + nta)
    elif number_r == 0 or number_r == 5:
        print(str(number) + tov)
    elif number_r == 6 or number_r == 7:
        print(str(number) + tov)
    elif number_r == 8 or number_r == 9:
        print(str(number) + tov)
    elif number_k == 11 or number_k == 12:
        print(str(number) + tov)
    elif number_k == 13 or number_k == 14:
        print(str(number) + tov)
    number += 1

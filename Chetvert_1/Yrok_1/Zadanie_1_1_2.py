# Для кубов нечётных чисел от 1 до 1000. Вычислить сумму чисел, сумма цифр кубов которых делится нацело на 7.
# При решении задачи использовать только арифмитическое операции и циклы.
# Не используем списки, функцию range, преобразование в строку/список.
#
# При решении задачи использовать только арифмитическое операции и циклы.
# Не используем списки, функцию range, преобразование в строку/список.
#
# Формат вывода результата:
# Вывод на экран формить в виде: xxxxxxx ^3: xxx; sum: xxx [сумма цифр]
#
# Например:
# 19 ^3: 6859 sum: 19 [ 28 ]
# 31 ^3: 29791 sum: 50 [ 28 ]
# 43 ^3: 79507 sum: 93 [ 28 ]
#
# Примеры:
# число 19, 19 ^ 3 = 6859, сумма чисел 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Поэтому 19 включаем в вывод.
#
# Алгоритм:
# Ваш алгоритм должен корректно работать и для интервала от 1 до 1000, но для любого числа(заведенного в код),
# например от 1 до 10000000.
# Сумма считается для самих чисел 19, 31, 43 и т.п. Не для кубов.
# Первый шаг - получить разряды числа(цифры), т.е. из 6859 получить отдельные цифры 6,8,5,9.
# Это делается за счет целочисленного деления на 10 и взятие остатка от этого деления.
# Не используйте операции со строками. Поэкспериментируйте.
# Вы не знаете заранее насколько большим(длинным) будет это число. Используйте цикл.
# Подумайте по какому условию вы из него выйдете. Отладьте этот алгоритм и подсчитайте сумму цифр.
# Для куба произвольного числа. Сделайте алгоритм предыдущего пунка частью цикла по числам от 1 до 1000 (нечетным).
# Подумайте как лаконично реализовать проход только по нечетным числам.

number = 0
number_n = int(input('Введите число: '))
number_h = 0

while number <= number_n:
    if number % 2 != 0:
        number_k = 0
        number_r = number ** 3
        number_m = number_r
        while number_r > 0:
            number_k = number_k + (number_r % 10)
            number_r = number_r // 10
        if (number_k % 7) == 0:
            number_h = number_h + number
            print(str(number) + ' ^3: ' + str(number_m) + ' sum: ' + str(number_h) + ' [ ' + str(number_k) + ' ]')
    number += 1
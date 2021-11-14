# 2. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield.
# Полностью истощить генератор.
#
# Техническое задание
# Отличие от задания 1 - только в использовании yield.
#
# Алгоритм
# Помните, что фукция генератор вызывается один раз, она возвращает объект-генератор и с ним дальше и работаем.
#
# Усложнение [одна звездочка]:
# С ключевым словом yield - как в задании 1: генератор нечётных чисел от 1 до n (включительно), для чисел,
# квадрат которых меньше 200.
# Усложнение [две звездочки]:
# С ключевым словом yield: Вычислять и возвращать само число и накопительную сумму этого и предыдущих чисел. Например:
#
# gen1 = iterator_with_yield(14)
# next(gen1)
# (1, 1)
# next(gen1)
# (3, 4)
# next(gen1)
# (5, 9)
# next(gen1)
# (7, 16)
# next(gen1)
# (9, 25)
# next(gen1)
# (11, 36)
# next(gen1)
# (13, 49)
# next(gen1)
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# StopIteration

def num_gen(num):
    for nun in range(1, num + 1, 2):
        yield nun

chis = num_gen(9)
for ank in chis:
    print(ank)

# 4. Задан список чисел. Необходимо создать список, содержащий те его элементы, значения которых больше предыдущего.
#
# Техническое задание
# Здесь нет условия создавать итератор/генератор. Можно использовать comprehensions.
# Формально первый элемент сравнить не с чем. Решите сами, что с ним делать: включать в новый список или нет.
# Можете сравнить его с последним элементом.
#
# Примеры/Тесты:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
#
# Алгоритм
# Как одновременно иметь доступ к текущему элементу списка и к предыдущему для их сравнения?
# Что для этого необходимо? Как сделать это без лишних вычислений? Какие варианты цикла for подойдут лучше всего?
# Помните: сортировка, поиск элемента в последовательности - очень затратные операции.
# Оцените эффективность вашего алгоритма. Смотри общие замечания к практическим заданиям.
# Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.


# Вариат.1 (Как мне было проще увидеть решение)
# def moi_gen():
#     kol_src = len(src)
#     for non in range(1, kol_src + 1):
#         if non == kol_src:
#             break
#         else:
#             perv = src[non - 1]
#             vtor = src[non]
#             if perv < vtor:
#                 result.append(vtor)
#                 yield result
#
#
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = []
#
# znch = moi_gen()
# for ank in znch:
#     pass
# print(result)

# Вариант.2 Попытался улучшить решение первого варианта.
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [src[non] for non in range(1, len(src) + 1) if non != len(src) if src[non - 1] < src[non]]
print(result)
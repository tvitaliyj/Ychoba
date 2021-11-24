# 3. Написать декоратор для логирования типов позиционных аргументов функции:
#
# Примеры/Тесты:
#
# def type_logger...;
#     ...;
#
# @type_logger
# def render_input(*args):
#    return 1
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# Call for: calc_cube
# 5: <class 'int'>
# Rezult: 125  type: <class 'int'>
#
# >>> render_input(1, a = 2, b = True, c = "q")
# Call for: render_input
# 1: <class 'int'>
# 'a' = 2: <class 'int'>, 'b' = True: <class 'bool'>, 'c' = q: <class 'str'>
# Rezult: 1  type: <class 'int'>
#
# Техническое задание:
# Если аргументов несколько - выводить данные о каждом через запятую.
# Все выводы должны быть в функции обертке(декораторе)
# После того как вы «обернули» функцию, «задекорировали» убедитесь что аргументы и
# возвращаемое значение остались как у исходной функции.
#
# Усложнение:
# вывести тип возвращаемого значения функции
# решить задачу для именованных аргументов
# вывести имя функции

def type_logger_1(element):
    def dekor_fyn(*args, **kwargs):
        print(*args, type(*args))
        detal_f = element(*args, **kwargs)
        return f'Rezult: {detal_f} type: {type(detal_f)}'
    return dekor_fyn

def type_logger_2(element):
    def dekor_fyn(*args, **kwargs):
        print(*args, type(*args))
        detal_f = element(*args, **kwargs)
        return detal_f
    return dekor_fyn

@type_logger_2
def render_input(*args, a, b, c):   # render_input(1, a = 2, b = True, c = "q")
    return f'a= {a} type: {type(a)}', f'a= {b} type: {type(b)}', f'a= {c} type: {type(c)}'

@type_logger_1
def calc_cube(x):   # calc_cube(5)
   return x ** 3

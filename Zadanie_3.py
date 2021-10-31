# 3. Дан список, содержащий искаженные данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита'].
# Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
#
# Формат вывода результата:
# Привет, Игорь!
# Привет, Марина!
# Привет, Николай!
# Привет, Аэлита!
#
# Техническое задание
# Список может содержать произвольное кол-во элементов.
# Имя сотрудника - всегда последнее слова в строке. Может содержать заглавные или строчные буквы в любом порядке.
# В результате имя сотрудника пишется строчными буквами и первая буква - заглавная.
#
# Алгоритм
# Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
# Нужен ли вам еще один список?
# Решив задачу, посмотрие внимательно: нет ли у вас лишних операций?

spisok_n = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
            'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for spisok in spisok_n:
    spisok = spisok.split()
    spisok = spisok[-1]
    srez_n = spisok[:1]
    srez_k = spisok[1:]
    srez = srez_n.upper() + srez_k.lower()
    print('Привет, ' + srez + '!')
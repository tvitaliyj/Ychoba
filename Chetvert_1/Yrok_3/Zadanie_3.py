# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
#
# Техническое задание
# Количество передаваемых имен в функцию может быть любым. Считаем, что переданы будут только корректные строки.
# Вернуть словарь с ключами, отсортированными в алфавитном порядке.
#
# Примеры/Тесты:
#
# >>> thesaurus()
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"],
#     "П": ["Петр"]
# }
#
# Алгоритм
# Вспомните как обработать произвольное количество передаваемых параметров.

def thesaurus(imia_n):
    baza_imen = {}
    spisok_sot = imia_n.split(' ')
    for spisok_so in spisok_sot:
        srez_n = spisok_so.upper()[0]
        srez_k = f'{srez_n}{spisok_so[1:]}'
        if baza_imen.get(srez_n) != None:
            srez_nk = baza_imen.setdefault(srez_n, srez_k)
            baza_imen[srez_n] = f'{srez_nk} {srez_k}'
        else:
            baza_imen[srez_n] = srez_k
    for baza_im in baza_imen.keys():
        baza_imen[baza_im] = baza_imen[baza_im].split()
    print(baza_imen)

imia_n = input('Введите имена сотрудников через пробел: ')
thesaurus(imia_n)

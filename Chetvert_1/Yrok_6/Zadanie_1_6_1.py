# 1. Распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
#
# Формат вывода результата:
#
# [
#     &#x2026;
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'HEAD', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_1'),
#     &#x2026;
# ]
#
# Техническое задание
# Не использовать библиотеки для парсинга. Только работа со строками.
# Создать список кортежей вида: `(<remote_addr>, <request_type>, <requested_resource>)`. Именно список кортежей.
# Код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# Вывести список на экран.
#
# Примечание:
# Файл логов можно загрузить отсюда:
# https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs
#
# Усложнение
# Уверены ли вы, что шаблон строк всегда одинаков? Попробуйте придумать как оценить идентичность шаблона строк файла.

from requests import get, utils
adres = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

konteiner_adresa = get(adres)
raskodirovka = utils.get_encoding_from_headers(konteiner_adresa.headers)
soderjimoe = (konteiner_adresa.content.decode(encoding=raskodirovka)).split(')"\n')

spisok = []

for non in soderjimoe:
    remote_addr = non[:non.find(' - - ')]
    request_type = non[non.find('] "') + 3:non.find(' /d')]
    requested_resource = non[(non.find('/dow')):non.find(' HTTP')]
    kartej = f'({remote_addr} {request_type} {requested_resource})'
    spisok.append(kartej)

    # print(non)
    # print(remote_addr)
    # print(request_type)
    # print(requested_resource)
    print(spisok)



# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, …)
# и возвращающую курс этой валюты по отношению к рублю.
#
# Формат вывода результата:
# Вызовите функцию для нескольких валют, обязательно для несуществующей валюты.
#
# Техническое задание
# Использовать библиотеку requests. В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
# В каком формате возвращен ответ?
# Функция принимает два аргумента: строка с URL, куда стучимся и строку с кодом валюты (только одной).
# Возвращает результат числового типа, например float. Если в качестве аргумента передали код валюты,
# которого нет в ответе, вернуть объект None.
# Для извлечения данных использовать только методы объект str.
# Сделать работу функции не зависящей от того, в каком регистре был передан аргумент.
# Функция должна корректно обрабатывать любой код валюты. Правильность параметра url можно не проверять.
# Вводить коды валют с клавиатуры (input) необязательно.
#
# Примеры/Тесты:
#
# >>> url = "<http://www.cbr.ru/scripts/XML_daily.asp>"
# >>> currency_rates(url, "USd")
# 71.7846
# >>> currency_rates(url, "EuR")
# 83.3347
# >>> currency_rates(url, "GBP")
# 98.3449
# >>> currency_rates(url, "GBP2")
# >>>
#
# Алгоритм
# Пример использования requests есть в методичке.
# Внимательно посмотрите все методы объекта str, которыми вы можете пользоваться. Обратите внимание,
# что у методов могу быть параметры, которые сильно облегчат вам работу.
# Помните, срез строки создает копию. Уверены ли вы, что вам нужна копия именно такого размера?
# Это увеличивает время выполнения и расходует память. Аналогично функция поиска требует времени для работы,
# можно ли оптимизировать поиск?
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом?
# Вспомните в каких случаях функция возвращает None.


def obmenik_valyt(url, val):
    from requests import get, utils

    konteiner_adresa = get(url)
    raskodirovka = utils.get_encoding_from_headers(konteiner_adresa.headers)
    soderjimoe = (konteiner_adresa.content.decode(encoding=raskodirovka)).split('ID')
    slovar_val = {}
    kon_znachenie = ''

    for soderjimoe_elm in soderjimoe:
        if soderjimoe_elm.find('</NumCode><CharCode>') > 0:
            poisk_klycha = soderjimoe_elm.find('</NumCode><CharCode>')
            klych = str(soderjimoe_elm[poisk_klycha + 20:poisk_klycha + 23])
            poisk_znachenia = soderjimoe_elm.find('</Name><Value>')
            znachenia = str(soderjimoe_elm[poisk_znachenia + 14:poisk_znachenia + 16])
            slovar_val[klych] = znachenia
    for slovar_va in slovar_val.keys():
        if slovar_va == val.upper():
            kon_znachenie = slovar_val[slovar_va]
            break
    if slovar_val.get(val.upper()) is None:
        kon_znachenie = ('None')
    return kon_znachenie

if __name__ == '__main__':
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    val = 'USd'

    print(obmenik_valyt(url, val))


# <?xml version="1.0" encoding="windows-1251"?><ValCurs Date="04.11.2021" name="Foreign Currency Market"><Valute
# ID="R01010"><NumCode>036</NumCode><CharCode>AUD</CharCode><Nominal>1</Nominal><Name>Австралийский доллар</Name><Value>53,2511</Value></Valute><Valute
# ID="R01020A"><NumCode>944</NumCode><CharCode>AZN</CharCode><Nominal>1</Nominal><Name>Азербайджанский манат</Name><Value>42,0763</Value></Valute><Valute
# ID="R01035"><NumCode>826</NumCode><CharCode>GBP</CharCode><Nominal>1</Nominal><Name>Фунт стерлингов Соединенного королевства</Name><Value>97,3733</Value></Valute><Valute
# ID="R01060"><NumCode>051</NumCode><CharCode>AMD</CharCode><Nominal>100</Nominal><Name>Армянских драмов</Name><Value>14,9587</Value></Valute><Valute
# ID="R01090B"><NumCode>933</NumCode><CharCode>BYN</CharCode><Nominal>1</Nominal><Name>Белорусский рубль</Name><Value>29,0624</Value></Valute><Valute
# ID="R01100"><NumCode>975</NumCode><CharCode>BGN</CharCode><Nominal>1</Nominal><Name>Болгарский лев</Name><Value>42,3530</Value></Valute><Valute
# ID="R01115"><NumCode>986</NumCode><CharCode>BRL</CharCode><Nominal>1</Nominal><Name>Бразильский реал</Name><Value>12,5858</Value></Valute><Valute
# ID="R01135"><NumCode>348</NumCode><CharCode>HUF</CharCode><Nominal>100</Nominal><Name>Венгерских форинтов</Name><Value>23,0512</Value></Valute><Valute
# ID="R01200"><NumCode>344</NumCode><CharCode>HKD</CharCode><Nominal>10</Nominal><Name>Гонконгских долларов</Name><Value>91,8663</Value></Valute><Valute
# ID="R01215"><NumCode>208</NumCode><CharCode>DKK</CharCode><Nominal>1</Nominal><Name>Датская крона</Name><Value>11,1346</Value></Valute><Valute
# ID="R01235"><NumCode>840</NumCode><CharCode>USD</CharCode><Nominal>1</Nominal><Name>Доллар США</Name><Value>71,4876</Value></Valute><Valute
# ID="R01239"><NumCode>978</NumCode><CharCode>EUR</CharCode><Nominal>1</Nominal><Name>Евро</Name><Value>82,8112</Value></Valute><Valute
# ID="R01270"><NumCode>356</NumCode><CharCode>INR</CharCode><Nominal>100</Nominal><Name>Индийских рупий</Name><Value>95,9501</Value></Valute><Valute
# ID="R01335"><NumCode>398</NumCode><CharCode>KZT</CharCode><Nominal>100</Nominal><Name>Казахстанских тенге</Name><Value>16,6852</Value></Valute><Valute
# ID="R01350"><NumCode>124</NumCode><CharCode>CAD</CharCode><Nominal>1</Nominal><Name>Канадский доллар</Name><Value>57,6141</Value></Valute><Valute
# ID="R01370"><NumCode>417</NumCode><CharCode>KGS</CharCode><Nominal>100</Nominal><Name>Киргизских сомов</Name><Value>84,2744</Value></Valute><Valute
# ID="R01375"><NumCode>156</NumCode><CharCode>CNY</CharCode><Nominal>1</Nominal><Name>Китайский юань</Name><Value>11,1745</Value></Valute><Valute
# ID="R01500"><NumCode>498</NumCode><CharCode>MDL</CharCode><Nominal>10</Nominal><Name>Молдавских леев</Name><Value>40,8501</Value></Valute><Valute
# ID="R01535"><NumCode>578</NumCode><CharCode>NOK</CharCode><Nominal>10</Nominal><Name>Норвежских крон</Name><Value>84,1050</Value></Valute><Valute
# ID="R01565"><NumCode>985</NumCode><CharCode>PLN</CharCode><Nominal>1</Nominal><Name>Польский злотый</Name><Value>18,0224</Value></Valute><Valute
# ID="R01585F"><NumCode>946</NumCode><CharCode>RON</CharCode><Nominal>1</Nominal><Name>Румынский лей</Name><Value>16,7344</Value></Valute><Valute
# ID="R01589"><NumCode>960</NumCode><CharCode>XDR</CharCode><Nominal>1</Nominal><Name>СДР (специальные права заимствования)</Name><Value>100,9612</Value></Valute><Valute
# ID="R01625"><NumCode>702</NumCode><CharCode>SGD</CharCode><Nominal>1</Nominal><Name>Сингапурский доллар</Name><Value>52,9773</Value></Valute><Valute
# ID="R01670"><NumCode>972</NumCode><CharCode>TJS</CharCode><Nominal>10</Nominal><Name>Таджикских сомони</Name><Value>63,4599</Value></Valute><Valute
# ID="R01700J"><NumCode>949</NumCode><CharCode>TRY</CharCode><Nominal>10</Nominal><Name>Турецких лир</Name><Value>74,2512</Value></Valute><Valute
# ID="R01710A"><NumCode>934</NumCode><CharCode>TMT</CharCode><Nominal>1</Nominal><Name>Новый туркменский манат</Name><Value>20,4542</Value></Valute><Valute
# ID="R01717"><NumCode>860</NumCode><CharCode>UZS</CharCode><Nominal>10000</Nominal><Name>Узбекских сумов</Name><Value>66,7360</Value></Valute><Valute
# ID="R01720"><NumCode>980</NumCode><CharCode>UAH</CharCode><Nominal>10</Nominal><Name>Украинских гривен</Name><Value>27,2276</Value></Valute><Valute
# ID="R01760"><NumCode>203</NumCode><CharCode>CZK</CharCode><Nominal>10</Nominal><Name>Чешских крон</Name><Value>32,3766</Value></Valute><Valute
# ID="R01770"><NumCode>752</NumCode><CharCode>SEK</CharCode><Nominal>10</Nominal><Name>Шведских крон</Name><Value>83,5506</Value></Valute><Valute
# ID="R01775"><NumCode>756</NumCode><CharCode>CHF</CharCode><Nominal>1</Nominal><Name>Швейцарский франк</Name><Value>78,3426</Value></Valute><Valute
# ID="R01810"><NumCode>710</NumCode><CharCode>ZAR</CharCode><Nominal>10</Nominal><Name>Южноафриканских рэндов</Name><Value>46,5590</Value></Valute><Valute
# ID="R01815"><NumCode>410</NumCode><CharCode>KRW</CharCode><Nominal>1000</Nominal><Name>Вон Республики Корея</Name><Value>60,5330</Value></Valute><Valute
# ID="R01820"><NumCode>392</NumCode><CharCode>JPY</CharCode><Nominal>100</Nominal><Name>Японских иен</Name><Value>62,7828</Value></Valute></ValCurs>

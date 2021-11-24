# 2. [Задача со звездочкой]: усложненный вариант задания 1. Написать скрипт, создающий из config_2.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Техническое задание
#
# Пример файла config_2.yaml можно скачать из прикрепленных к уроку файлов. Или его можно создать в любом текстовом редакторе «руками» (не программно).
# Не используйте библиотеки для работы с YAML, проведите парсинг вручную - это несложно.
# Подумайте о возможных исключениях при работе скрипта.
# Алгоритм
#
# Чтобы распарсить YAML файл, внимательно проанализируйте его структуру: как в файле обозначен следующий уровень папок.
# Здесь надо немного повозиться с уровнями вложенности папок. Для каждой строки мы либо уходим «вглубь» и путь нарастает, либо возвращаемся «наверх» и надо убрать лишние элементы из пути.
# Создание файла отличается от создания директории: на Windows используйте для этого «открыть для записи и ничего не записать», на linux - mknod. Помните о переносимости кода между ОС.

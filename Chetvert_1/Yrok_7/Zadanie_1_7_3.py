# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates:
#
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
#
# Техническое задание
# В папках mainapp, authapp и аналогичных могут быть и другие файлы, кроме приведенных в примере.
# Папку templates надо создать внутри исходной директории, в примере - внутри my_project
# Шаблон - это папка templates. Ее уровень в структуре папок может быть любым.
# Исходные файлы и папки необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках (они играют роль пространств имён).
# Предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.

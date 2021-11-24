# 5. [Задача со звездочкой]: усложненный вариант задания 4. Написать скрипт,
# который для заданной папки выводит статистику размеров файлов по расширениям.
#
# Формат вывода результата:
#
# {
#     100: [15, [txt']],
#     1000: [3, ['py', 'txt']],
#     10000: [7, ['html', 'css']],
#     100000: [2, ['png', 'jpg']]
#   }
#
# Техническое задание
# Директорию с файлами some_data_adv можно скачать из прикрепленных к уроку файлов.
# Результат возвращается в виде словаря
# ключи — верхняя граница размера файла (пусть будет кратна 10) - как в задании 4.
# значения — списки вида [<files_quantity>, [<files_extensions_list>]]. В список <files_extensions_list> заносятся все расширения для файлов удовлетворяющих условию размера, без повторений.
# Словарь сохраните в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

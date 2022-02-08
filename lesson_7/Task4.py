# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи —
# верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
import os
import shutil


rang = [10**x for x in range(1, 5)]
ranges = [0]
ranges.extend(rang)
files_in_range = {x: 0 for x in ranges}
source_dir = os.path.join(r'my_project1')

for roots, dirs, files in os.walk(source_dir):
    for file in files:
        filesize = os.stat(os.path.join(roots, file)).st_size
        for i in range(1, len(ranges)):
            if filesize < ranges[i] and ranges[i-1] <= filesize:
                files_in_range[ranges[i-1]] = files_in_range[ranges[i-1]] + 1

print(files_in_range)
# Есть два файла: в одном хранятся ФИО пользователей сайта, а в
# другом — данные об их хобби. Известно, что при хранении данных
# используется принцип: одна строка — один пользователь, разделитель
# между значениями — запятая. Написать код, загружающий данные из обоих
# файлов и формирующий из них словарь: ключи — ФИО, значения — данные о
# хобби. Сохранить словарь в файл. Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле
# с ФИО, задаём в словаре значение None.
# Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во
# много раз меньше объема ОЗУ.
import csv

users_hobby = {}
with open('users.csv', 'r', encoding='utf-8') as u_file:
   l_users = []
   for line1 in csv.reader(u_file, delimiter=','):
       user_n = ' '.join(line1)
       l_users.append(user_n)

with open('hobby.csv', 'r', encoding='utf-8') as h_file:
    l_hobby = []
    for line1 in csv.reader(h_file, delimiter=','):
        l_hobby.append(line1)

if len(l_users) < len(l_hobby):
    exit(1)

for cnt in range(0, len(l_users)):
    if cnt >= len(l_hobby):
        n_hobby = None
    else:
        n_hobby = l_hobby[cnt]
    users_hobby.update({l_users[cnt]: n_hobby})

print(users_hobby)

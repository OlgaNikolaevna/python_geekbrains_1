# Реализовать простую систему хранения данных о суммах продаж булочной.
# Должно быть два скрипта с интерфейсом командной строки: для записи данных
# и для вывода на экран записанных данных. При записи передавать из командной
# строки значение суммы продаж. Для чтения данных реализовать в командной
# строке следующую логику:
# просто запуск скрипта — выводить все записи;
import csv

FILE_NAME = 'bakery.csv'


def add_sale(value):
    with open(FILE_NAME, 'a+', encoding='utf-8', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=';')
        csvwriter.writerow([value])


def show_sales(line_st = None, line_end = None):
    with open(FILE_NAME, 'r', encoding='utf-8') as csvfile:
        all_sales = []
        csvreader = csv.reader(csvfile, delimiter=';')
        row_count = sum(1 for row in csvreader)
        csvfile.seek(0)
        if line_st is None:
            line_st = 0
        else:
            line_st = line_st -1

        if line_end is None:
            line_end = row_count
        else:
            line_end = min(line_end, row_count)

        for cnt in range(0, line_end):
            if cnt < line_st:
                csvreader.__next__()
            else:
                all_sales.append(csvreader.__next__())
    print(all_sales)


add_sale(1551)
add_sale(1552)
show_sales()
show_sales(3, 4)


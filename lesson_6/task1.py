# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]

with open('nginx_logs.txt', 'r', encoding='utf-8') as rfile:
   l_adr = []
   #(<remote_addr>, <request_type>, <requested_resource>)
   for line in rfile:
       split_1 = line.split(' - - ')
       remote_addr= split_1[0]
       split_2 = split_1[1].split('"')[1].split(' /')
       request_type = split_2[0]
       requested_resource = split_2[1]
       adr = (remote_addr, request_type, requested_resource)
       l_adr.append(adr)
print(l_adr)


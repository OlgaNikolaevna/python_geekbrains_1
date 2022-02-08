#  Написать скрипт, создающий стартер (заготовку) для проекта со следующей
#  структурой папок:
# |--my_project
#    |--settings
#    |--authapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена
# папок под конкретный проект; можно ли будет при этом расширять конфигурацию и хранить
# данные о вложенных папках и файлах (добавлять детали)?

import os

proj_file_struct = {'root_name': 'my_project',
                    'dought_name': ['settings', 'authapp', 'adminapp', 'authapp']}

dir_path = os.path.join(proj_file_struct.get('root_name'))
if not os.path.exists(dir_path):
   os.mkdir(dir_path)

for d_path in proj_file_struct.get('dought_name'):
   dougt_path = os.path.join(proj_file_struct.get('root_name')+ r'//' + d_path)
   if not os.path.exists(dougt_path):
      os.mkdir(dougt_path)

# Здесь удобно менять имена папок, добавлять новые.
# Чтобы еще больше универсанилизировать решение можно спролтзовать структтуру,
# где каждым объектом является словарь. Но возможно это плохое решение..
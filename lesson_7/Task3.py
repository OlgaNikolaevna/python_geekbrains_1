#Написать скрипт, который собирает все шаблоны в одну папку templates
import os
import shutil

source_dir = os.path.join(r'my_project1')
res_dir = os.path.join(r'my_project1\templates')

if not os.path.exists(res_dir):
   os.mkdir(res_dir)

for roots, dirs, files in os.walk(source_dir):
    if roots.count('templates'):
        # копируем папки:
        for s_dir in  dirs:
            new_dir = os.path.join(res_dir, s_dir)
            if not os.path.exists(new_dir):
                os.mkdir(new_dir)
                print('created dir ' + new_dir)
        # копируем файлы:
        for s_file in files:
            s_file_path = os.path.join(roots, s_file)
            r_file_path = os.path.join(res_dir, os.path.basename(roots))
            if r_file_path != os.path.dirname(s_file_path):
                shutil.copy(s_file_path, r_file_path)
                print('copied ' + s_file_path + ' to ' + r_file_path)



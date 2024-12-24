import os

import datetime


for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        datetime_obj = datetime.datetime.fromtimestamp(filetime)
        # formatted_time = file.localtime() # time.strftime("%d.%m.%Y %H:%M", filetime.localtime(filetime))
        filesize = os.stat(filepath).st_size
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {datetime_obj}, '
              f'Родительская директория: {parent_dir}')


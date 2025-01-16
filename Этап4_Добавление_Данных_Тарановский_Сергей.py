# Grade 1. Этап 4: Задание 4
# Задание: Добавление данных в файл

import yaml

# Добавление заметок в файл без удаления существующих
def append_notes_to_file(notes, filename):
    # Аргумент 'a' создаст файл если его не было и добавит данные
    with open(filename, 'a', encoding='utf-8') as file:
        y_file = yaml.dump(notes, file, allow_unicode=True, sort_keys=False)


username = input('Введите имя пользователя: ').capitalize()
title = input('Введите заголовок: ').capitalize()
content = input('Введите описание: ').capitalize()
status = input('Введите статус: ').capitalize()
created_date = input('Дата создания: ').capitalize()
issue_date = input('Дедлайн: ').capitalize()

note = [{'Имя пользователя': username,
        'Заголовок': title,
        'Описание': content,
        'Статус': status,
        'Дата создания': created_date,
        'Дедлайн': issue_date
        }]

filename = 'notes.yml'

append_notes_to_file(note, filename)

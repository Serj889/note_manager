# Grade 1. Этап 4: Задание 1
# Задание: Записывает список заметок (notes) в текстовый файл (filename).

import yaml

# Функция записи заметки в файл
def save_notes_to_file(notes, filename):
    # Атрибут 'w' создаст новый файл и запишет в него полученный словарь
    with open(filename, 'w', encoding='utf-8') as file:
        # Параметр 'allow_unicode=True' позволяет добавлять кирилицу
        # Параметр 'sort_keys=False' сохраняет словарь в порядке ввода, без дополнительной сортировки
        yaml.dump(notes, file, allow_unicode=True, sort_keys=False)
       

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
        'Дедлайн': issue_date}]

save_notes_to_file(note, 'notes.yml')

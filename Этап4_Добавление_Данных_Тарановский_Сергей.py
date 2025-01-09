# Grade 1. Этап 4: Задание 4
# Задание: Добавление данных в файл

# Добавление заметок в файл без удаления существующих
def append_notes_to_file(notes, filename):
    # Аргумент 'a' создаст файл если его не было и добавит данные
    file = open(filename, 'a', encoding='utf-8')
    file.write('\n'.join(map(str, notes)))
    # Следующая заметка добавится с новой строки
    file.write('\n---' + '\n')
    file.close()


username = input('Введите имя пользователя: ')
title = input('Введите заголовок: ')
content = input('Введите описание: ')
status = input('Введите статус: ')
created_date = input('Дата создания: ')
issue_date = input('Дедлайн: ')

note = ['Имя пользователя: ' + username,
        'Заголовок: ' + title,
        'Описание: ' + content,
        'Статус: ' + status,
        'Дата создания: ' + created_date,
        'Дедлайн: ' + issue_date
        ]

append_notes_to_file(note, 'notes.txt')

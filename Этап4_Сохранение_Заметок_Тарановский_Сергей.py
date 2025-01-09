# Grade 1. Этап 4: Задание 1
# Задание: Записывает список заметок (notes) в текстовый файл (filename).

def save_notes_to_file(notes, filename):
    file = open(filename, 'w', encoding='utf-8')
    file.write('\n'.join(map(str, notes)))
    file.write('\n---')
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
        'Дедлайн: ' + issue_date]

save_notes_to_file(note, 'notes.txt')

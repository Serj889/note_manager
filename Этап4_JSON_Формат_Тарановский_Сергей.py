# Grade 1. Этап 4: Задание 5.
# Задание: Сохраняет заметки в формате JSON

import json     # Импорт библиотеки JSON


def save_notes_to_json(notes, filename):        # Функция для записи в файл
    # Открытие файла для записи и создание файла при его отсутствии
    with open(filename, 'w+', encoding='utf-8') as file:
        # Команда для записи в файл в структуре JSON с наличием кирилицы и отступом каждой строки на 4 пробела
        json.dump(notes, file, indent=4, ensure_ascii=False)
        file.write('\n')


note = []       # Объявление списка в котором будут хранится словари
add_note = ''   # Начальная позиция цикла

while add_note != 'Нет':            # Выход из цикла добавления записей по слову Нет
    add_note = input('Добавить заметку (да/нет): ').capitalize()
    if add_note == 'Да':            # Заполнение данных от пользователя
        username = input('Введите имя пользователя: ').capitalize()
        title = input('Введите заголовок: ').capitalize()
        content = input('Введите описание: ').capitalize()
        status = input('Введите статус: ').capitalize()
        created_date = input('Дата создания: ')
        issue_date = input('Дедлайн: ')

        note_01 = {'Имя пользователя: ': username,      # Создание словаря с заметкой
                   'Заголовок: ': title,
                   'Описание: ': content,
                   'Статус: ': status,
                   'Дата создания: ': created_date,
                   'Дедлайн: ': issue_date}
        note.append(note_01)            # Добавление словаря в список
    elif add_note == 'Нет':
        print('Ввод окончен.')
        break
    else:
        # Если ответ пользователя отличается от Да/Нет
        print('Ответ неясен. Повторите ввод')

# Вызов функции передача имени файла и списка со словарями
save_notes_to_json(note, 'notes.json')

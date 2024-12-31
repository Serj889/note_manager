# Grade 1. Этап 4: Задание 2
# Задание: Загрузка заметок из файла

import ast


def load_notes_from_file(filename):         # Функция чтения из файла
    note = []                               # Обозначение списка
    try:
        # попытка открыть заданный файл
        file = open(filename, 'r', encoding='utf-8')
    except FileNotFoundError:                           # Обработка ошибки если такого файла нет
        note = 'Файл не найден.'
    else:                                               # Чтение из файла
        # Чтение всего содержимого файла по строкам
        note_002 = file.readlines()
        if len(note_002) == 0:                          # Ответ пользователю если файл пуст
            note = 'Записей нет.'
            return (note)
        else:
            for i in range(len(note_002)):
                # Преобразование строк в словарь
                note_001 = ast.literal_eval(note_002[i])
                # Создание словаря из строки файла
                note.append(note_001)
        file.close()                                        # Закрытие файла
    return (note)


# Запуск функции чтения из файла
notes = load_notes_from_file('example_01.txt')
if notes == 'Файл не найден.':
    print(notes)
elif notes == 'Записей нет.':
    print('Файл не содержит записей.')
else:
    # Вывод заметки из файла на экран
    for i in range(len(notes)):
        for x, y in notes[i].items():
            print(f'{x}: {y}')
        print('---------------------')

# Grade 1. Этап 4: Задание 3
# Задание: Обработка ошибок.


def load_notes_from_file(filename):         # Функция чтения из файла
    note_fin = []       # Список словарей
    note_list = ''      # Список одной заметки
    try:
        # попытка открыть заданный файл
        file = open(filename, 'r', encoding='utf-8')
    except FileNotFoundError:                                   # Обработка ошибки если файл не найден
        file = open(filename, 'w', encoding='utf-8')            # Создание пустого файла
        note = f'Файл {filename} не найден.'
    except EOFError:                                            # ошибка чтения из файла
        note = f'Ошибка чтения файла {filename}.'
    else:
        note = file.readline()                                  # Чтение первой строки файла
        if note == '':
            note = 'Записей нет.'               # Сообщение если файл пуст
        else:
            while note != '':                   # Проверяем на конец файла
                new_note = {}                   # Создаем новый временный словарь

                if note == '-----' or note == '-----\n':        # Проверяем на конец заметки
                    # Меняем символы переноса строки и ':' на запятые
                    note_list = note_list.replace('\n', ',').replace(': ', ',')
                    # Разбиваем строку на список по ','
                    note_list = note_list.split(',')

                    # Собираем словарь из нового списка
                    # Нечетным элементам строки присваиваем четные элементы строки
                    for k in range(0, len(note_list)-1, 2):
                        v = k + 1
                        new_note[note_list[k]] = note_list[v]
                    # Добавляем получившийся словарь в итоговый список
                    note_fin.append(new_note)
                    note_list = ''      # Обнуляем список в который собираем заметку
                else:
                    note_list = note_list + note    # Собираем все строки заметки в один список

                note = file.readline()      # Считываем следующую строку из файла
            note = note_fin                 # Передаем список словарей на переменную выхода

        file.close()            # Закрытие файла
    return (note)


# Запуск функции чтения из файла
filename = 'example_R_02.txt'
notes = load_notes_from_file(filename)

if notes == 'Файл не найден.':                  # Сообщение если файл не найден
    print(notes)
    print(f'Новый файл {filename} создан.')
elif notes == 'Записей нет.':                   # Сообщение если файл пустой
    print(f'Файл {filename} не содержит записей.')
else:                                           # Вывод списка словарей
    print(notes)

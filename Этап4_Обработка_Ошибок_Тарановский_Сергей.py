# Grade 1. Этап 4: Задание 3
# Задание: Обработка ошибок.


def load_notes_from_file(filename):         # Функция чтения из файла
    try:
        # Попытка открыть файл
        with open(filename, 'r', encoding='utf-8') as file:
            notes = f'Файл "{filename}" успешно открыт.'
            return(notes)

    except FileNotFoundError:
        # Если файл не найден, выводим сообщение об ошибке
        notes = 'Файл не найден.'
        return(notes)

    except IOError:
        # Если возникает ошибка ввода-вывода, выводим сообщение об ошибке
        notes = f'Произошла ошибка ввода-вывода при чтении файла "{filename}"!'
        return(notes)

    except Exception as e:
        # Обработка других ошибок
        notes = f'Произошла непредвиденная ошибка: {e}'
        return(notes)


# Запуск функции чтения из файла
filename = 'notes.txt'
notes = load_notes_from_file(filename)

if notes == 'Файл не найден.':                  # Сообщение если файл не найден
    print(notes)
    with open(filename, 'w', encoding='utf-8') as file:
        print(f'Новый файл {filename} создан.')
elif notes == 'Записей нет.':                   # Сообщение если файл пустой
    print(f'Файл {filename} не содержит записей.')
else:                                           # Вывод списка словарей
    print(notes)

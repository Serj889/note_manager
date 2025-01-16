# Grade 1. Этап 4: Задание 2
# Задание: Загрузка заметок из файла

import yaml

def load_notes_from_file(filename):         # Функция чтения из файла
    try:
        # Попытка открыть файл
        with open(filename, 'r', encoding='utf-8') as file:
            # Чтение содержимого файла
            notes = yaml.load(file, Loader=yaml.FullLoader)
            return(notes)

    except FileNotFoundError:
        # Если файл не найден, выводим сообщение об ошибке
        notes = f'Файл "{filename}" не найден!'
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
filename = 'notes.yml'
notes = load_notes_from_file(filename)

if notes == None:
    print('Указанный файл пуст.')
else:
    # Вывод списка словарей
    print(notes)

# Grade 1. Этап 2: Задание 2
# Задание: Проверка и обновление статуса заметки


# Список возможных статусов заметки
dict_of_status = {'1': 'Выполнено', '2': 'В процессе', '3': 'Отложено'}
# Начальный статут заметки
status = dict_of_status['2']
print(f'Текущий статус заметки: "{status}"')
print('Выберите новый статус заметки:')

# Вывод списка варинтов статуса для пользователя
for i in range(1, len(dict_of_status)+1):
    print(f'{i} - {dict_of_status[str(i)]}')

while status != '':
    # Запрос ввода от пользователя статуса соответствующей цифрой,
    # строкой или кнопки ENTER для выхода.
    # Приведение введеной строки к стилю в словаре.
    status = input(
        'Введите номер или слово нового статуса или нажмите ENTER для выхода: ').capitalize()
    # Проверка введенного значения по ключам словаря.
    if status in dict_of_status.keys():
        status = dict_of_status[status]
        break
    # Проверка введенного значения по значениям словаря.
    elif status in dict_of_status.values():
        break
    else:
        print('Новое значение статуса не определено.')
else:
    status = dict_of_status['2']

print('')
# Вывод окончательного статуса заметки
print(f'Установлен статус заметки: "{status}"')
print('')

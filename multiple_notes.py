# Grade 1. Этап 2: Задание 4
# Задание: Работа с несколькими заметками


from datetime import datetime       # Вызов библиотеки datetime


def make_dict(id_note):                            # Функция создания заметки
    all_dict = {'ID:': '',
                'Имя:': '',
                'Заголовок:': '',
                'Описание:': '',
                'Статус:': '',
                'Дата создания:': '',
                'Дедлайн:': ''}

    def check_user_date(user_date):         # Функция проверки правильного формата даты
        while True:
            # Запрос пользовательской даты
            issue_date = input(
                f'Введите дату {user_date} (день-месяц-год или год-месяц-день): ')
            try:
                # проверка на формат дд-мм-ГГГГ
                value_date = datetime.strptime(issue_date, '%d-%m-%Y').date()
                break
            except ValueError:                          # Игнорирование ошибки о неправильном значении даты
                try:
                    # Проверка введеной даты на формат ГГГГ-мм-дд
                    value_date = datetime.strptime(
                        issue_date, '%Y-%m-%d').date()
                    # Перевод даты в формат дд-мм-ГГГГ
                    issue_date = value_date.strftime('%d-%m-%Y')
                    break
                except ValueError:                      # Игнорирование ошибки о неправильном значении даты
                    print('')
                    # Вывод сообщения для пользователя о недопустимом формате даты
                    print(
                        'Убедитесь, что вводите дату в формате день-месяц-год или год-месяц-день, например: 01-12-2024.')
                    print('')
                    continue                            # Переход к началу цикла о запросе даты
        # Возврат значения даты в соответствующую переменную
        return (issue_date)

    for i in all_dict.keys():               # Запрос пользовательских данных по имеющимся полям
        if i == 'ID:':                      # Установка ID заметки
            all_dict['ID:'] = id_note
            continue
        if i == 'Дата создания:':           # Запрос даты создания заметки с использованием функции проверки даты
            all_dict['Дата создания:'] = check_user_date('создания')
        elif i == 'Дедлайн:':               # Запрос даты дедлайна заметки с использованием функции проверки даты
            all_dict['Дедлайн:'] = check_user_date('дедлайна')
        elif i == 'Статус:':                # Запрос статуса с предложениями ввода
            all_dict[i] = input(
                f'Введите статус заметки (новая, в процессе, выполнено): ')
        else:
            # Ввод пользовательских значений
            all_dict[i] = input(f'Введите {i} ')
            # Значения по умолчанию для пустого заголовка
            if all_dict['Заголовок:'] == '':
                all_dict['Заголовок:'] = 'Пустой заголовок'
            # Значения по умолчанию для пустого описания
            elif all_dict['Описание:'] == '':
                all_dict['Описание:'] = 'Без описания'
    return (all_dict)                     # Возврат готового словаря


list_notes = []     # Создание списка
count_note = 1000   # Счетчик заметок и их ID
print('\nДобро пожаловать в "Менеджер заметок"!')

# Условие работы цикла по созданию заметок, выполняется пока пользоваатель не скажет 'нет'
making_note = True

while making_note:
    # Ввод ответа не зависит от регистра
    add_note = input(
        '\nВы хотите добавить новую заметку? "Да/Нет": ').capitalize()
    if add_note == 'Да':
        count_note += 1
        print('\nСоздание новой заметки.')
        # Добавление полученных данных в основной словарь
        list_notes.append(make_dict(count_note))
    elif add_note == 'Нет':
        # Прерывание цикла
        making_note = False
    else:
        print('Некорректный ответ')

if list_notes == []:
    print('\nВы не создали ни одной заметки.')
else:
    print(f'\nКоличество заметок: {len(list_notes)}')
    print()
    # Вывод на экран списка каждый элемент которого является отдельной заметкой
    for i in range(len(list_notes)):
        print(f'Заметка {i + 1}.')
        # Вывод каждой заметки в виде словаря
        for keys_00, value_00 in list_notes[i].items():
            print(keys_00, value_00)
        print('')

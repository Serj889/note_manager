# Grade 1. Этап 3: Задание 5
# Задание: Создание меню действий


from datetime import datetime, timedelta       # Вызов библиотеки datetime


# Функция создания заметки, входное значение "количество заметок"
def make_dict(id_note):
    all_dict = {'ID:': '',                  # Поля для заполнения пользователем
                'Имя:': '',
                'Заголовок:': '',
                'Описание:': '',
                'Статус:': '',
                'Дата создания:': '',
                'Дедлайн:': ''}

    for i in all_dict.keys():                       # Запрос пользовательских данных по имеющимся полям
        if i == 'ID:':                              # Установка ID заметки
            all_dict['ID:'] = id_note
            continue
        if i == 'Дата создания:':                   # Запрос даты создания заметки с использованием функции проверки даты
            # Функция проверки даты с определенным агрументом
            all_dict['Дата создания:'] = check_user_date('создания')
        elif i == 'Дедлайн:':                       # Запрос даты дедлайна заметки с использованием функции проверки даты
            # Функция проверки даты с определенным агрументом
            all_dict['Дедлайн:'] = check_user_date('дедлайна')
        elif i == 'Статус:':                        # Запрос статуса с предложениями ввода
            # Функция проверки введенного статуса
            all_dict['Статус:'] = status_note()

        else:
            # Ввод пользовательских значений
            all_dict[i] = input(f'Введите {i} ').capitalize()
            # Значения по умолчанию для пустого заголовка
            if all_dict['Заголовок:'] == '':
                all_dict['Заголовок:'] = 'Пустой заголовок'
            # Значения по умолчанию для пустого описания
            elif all_dict['Описание:'] == '':
                all_dict['Описание:'] = 'Без описания'
    print('Новая заметка создана!')
    return (all_dict)                     # Возврат готового словаря


def display_notes(notes):  # Функция вывода заметок на экран
    # Номер заметки 'ID' присутствует при любом выводе
    keys_id = 'ID:'
    print('\nЧто вы хотите вывести на экран?')         # Меню для пользователя
    # Что пользователь хочет вывести на экран
    view_note = ['1 - Полностью все заметки.',
                 '2 - Только заголовки заметок.',
                 '3 - Только статусы заметок.',
                 '4 - Сортировка всех заметок по Дате создания.',
                 '5 - Сортировка всех заметок по дате Дедлайна.',
                 '6 - Вывод по номеру заметки (без сортировки)'
                 ]
    print('\n'.join(view_note))
    print_note = input('Введите номер меню: ')

    print(f'\nКоличество ваших заметок: {len(notes)}.')
    # Ошибочный выбор пункта меню
    if print_note not in ('1', '2', '3', '4', '5', '6'):
        print('Команда не распознана.')
        return

    elif print_note == '2':                     # Выбор только заголовков
        print('Вот текущий список ваших заголовков:')
        print('-------------------------')
        keys_note = 'Заголовок:'

    elif print_note == '3':                     # Выбор только статусов заметок
        print('Вот текущий список статусов ваших заметок:')
        print('-------------------------')
        keys_note = 'Статус:'

    elif print_note == '4':                     # Сортировка заметок по дате создания
        print('Сортировка по дате создания.')
        print('-------------------------')
        # Вызов функции сортировки с аргументами: (список заметок и Дата создания)
        notes, print_note = sort_note(notes, print_note)

    elif print_note == '5':                     # Сортировка заметок по дате дедлайна
        print('Сортировка по дате дедлайна.')
        print('-------------------------')
        # Вызов функции сортировки с аргументами: (список заметок и Дата дедлайна)
        notes, print_note = sort_note(notes, print_note)

    # Сортировка заметок по номеру заметки (ID)
    elif print_note == '6':
        notes.sort(key=lambda note_01: note_01['ID:'])
        print_note = '1'

    if print_note == '1':
        # Вывод на экран списка каждый элемент которого является отдельной заметкой
        for i in range(len(notes)):
            # Вывод каждой заметки в виде словаря
            for keys_00, value_00 in notes[i].items():
                # Вывод данных ровными столбцами
                print('{:<16} {:<15}'.format(keys_00, value_00))
            print('-------------------------')
        return
    # Вывод на экран списка каждый элемент которого является отдельной заметкой
    for i in range(len(notes)):
        # Вывод каждой заметки в виде словаря
        for keys_00, value_00 in notes[i].items():
            if keys_00 == keys_note or keys_00 == keys_id:
                # Вывод данных ровными столбцами
                print('{:<16} {:<15}'.format(keys_00, value_00))
        print('-------------------------')


def sort_note(notes_in, choose_in):         # Функция сортировки заметок по дате
    if choose_in == '4':
        data_arg = 'Дата создания:'
    elif choose_in == '5':
        data_arg = 'Дедлайн:'

    for i in notes_in:                                              # Перевод всех дат из str в формат даты
        i[data_arg] = datetime.strptime(i[data_arg], '%d-%m-%Y')

    # Сортировка дат
    notes_in.sort(key=lambda i: i[data_arg])

    for i in notes_in:                                              # Обратный перевод всех дат в формат str
        i[data_arg] = datetime.strftime(i[data_arg], '%d-%m-%Y')
    # Возвращение отсортированного списка заметок и маркер для вывода на экран всего списка.
    return (notes_in, '1')


def status_note():          # Функция проверки ввода статуса
    status = input(
        f'Введите статус заметки (Новая, В процессе, Выполнено): ').capitalize()
    # Проверка статуса на соответствие предложенным вариантам
    while status not in ('Новая', 'В процессе', 'Выполнено'):
        status = input(
            f'Выберите один из предложенных вариантов (Новая, В процессе, Выполнено): ').capitalize()
    # Возвращение в программу значения введенного статуса
    return (status)


# Функция проверки правильного формата даты, входное значение "создание" или "дедлайн"
def check_user_date(user_date):
    while True:
        # Запрос пользовательской даты
        issue_date = input(
            f'Введите дату {user_date} (день-месяц-год или нажмите ENTER для автоматичекой установки): ')
        # Установка сегодняшней даты, если пользователь ничего не ввел
        if issue_date == '' and user_date == 'создания':
            # Запрос сегодняшней даты
            today = datetime.today().date()
            issue_date = today.strftime('%d-%m-%Y')
        elif issue_date == '' and user_date == 'дедлайна':
            # Установка даты дедлайна на неделю позже сегодняшнего числа
            today = datetime.today().date() + timedelta(days=7)
            issue_date = today.strftime('%d-%m-%Y')
        try:
            # проверка на формат дд-мм-ГГГГ
            value_date = datetime.strptime(issue_date, '%d-%m-%Y').date()
            break
        except ValueError:              # Игнорирование ошибки о неправильном значении даты
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
                    'Убедитесь, что вводите дату в формате день-месяц-год или нажмите ENTER для автоматичекой установки')
                print('')
                continue                            # Переход к началу цикла о запросе даты
    # Возврат значения даты в соответствующую переменную
    return (issue_date)


# Функция подтверждения изменения или удаления заметки
def conf_change(do_note):
    conf_del_note = 'V'             # Временная переменная для запуска цикла
    if do_note == 'удалить':         # Корректное отображение обращения к пользователю
        do_note_01 = 'удалена'
    elif do_note == 'изменить':
        do_note_01 = 'изменена'

    while conf_del_note != 'Нет':       # Цикл на подтверждение изменения
        # Запрос Да/Нет не зависит от регистра
        conf_del_note = input(
            f'Вы уверены что хотите {do_note} заметку? Да/Нет - ').capitalize()
        if conf_del_note == 'Да':                   # Подтверждение введеных изменений
            print(f'Заметка успешно {do_note_01}.')
            break
        elif conf_del_note == 'Нет':                # Отмена введеных изменений
            print('Действие отменено.')
            break
        else:
            print('Команда не распознана.')
    # Возврат пользовательского ответа (да/нет)
    return (conf_del_note)


# Функция редактирования полей заметки
def upd_note(upd_dict):
    pole = input('Какое поле вы хотите отредактировать: ').capitalize()
    pole = pole + ':'
    if pole in ('Id:', 'Дата создания:'):               # эти поля не должны редактироватся
        print('Данное поле нельзя отредактировать.')
    elif pole == 'Статус:':
        # Переход в функцию проверки статуса
        upd_dict[pole] = status_note()
    elif pole == 'Дедлайн:':
        # Переход в функцию проверки введенной даты
        upd_dict[pole] = check_user_date('дедлайна')
    elif pole in upd_dict.keys():
        upd_dict[pole] = input('Введите новое значение поля: ')
    else:
        print('Такого поля не обнаружено.')
    return (upd_dict)                   # Возвращение отредактированной заметки


# Функция поиска заметок по ключевому полю и/или статусу
def search_notes(notes, keyword=None, status=None):
    # Временный словарь хранения выбранных заметок
    temp_note = []
    if keyword is not None and status is None:          # Условие если не объявлена переменная 'Status'
        for i in range(len(notes)):
            # Проверка содержания ключевого слова и что ключевое слово не является указанием статуса
            if keyword in notes[i].values() and keyword not in ('Новая', 'В процессе', 'Выполнено'):
                temp_note.append(notes[i])
    elif keyword is None and status is not None:        # Условие если не объявлено ключевое слово 'Keyword'
        for i in range(len(notes)):
            if status in notes[i].values():
                temp_note.append(notes[i])
    else:                                               # Если объявлены оба условия
        for i in range(len(notes)):
            if status in notes[i].values() and (keyword in notes[i].values() and keyword not in ('Новая', 'В процессе', 'Выполнено')):
                temp_note.append(notes[i])

    if temp_note == []:                                 # Ответ если совпадений не найдено
        print('\nСовпадений не найдено.')

    return (temp_note)


list_notes = []     # Создание списка
count_note = 1000   # Счетчик заметок и их ID
choose_do = ['1 - Добавить заметку.',               # Меню доступных для пользователя действий
             '2 - Просмотреть все заметки.',        # У пользователя запрашивается номер пункта
             '3 - Редактировать заметку.',
             '4 - Удалить заметку.',
             '5 - Поиск по заметкам.',
             '6 - Выход.'
             ]

print('\nДобро пожаловать в "Менеджер заметок"!\n')

# Условие работы цикла по созданию заметок, выполняется пока пользоваатель не выберет 'Выход'
making_note = True

while making_note:
    print()
    print('\n'.join(choose_do))             # Вывод пользовательского меню
    # Ввод ответа не зависит от регистра
    add_note = input(
        'Что вы хотите сделать? (Введите номер): ')

    if add_note == '1':
        # Команда 'Добавить заметку.'
        count_note += 1
        print('\nСоздание новой заметки.')
        # Добавление полученных данных в основной словарь через функцию make_dict
        list_notes.append(make_dict(str(count_note)))

    elif add_note == '2':       # Команда на просмотр всех заметок
        if list_notes == []:
            print('\nВы не создали ни одной заметки.')
        else:
            display_notes(list_notes)

    elif add_note == '3':       # Редактирование заметки
        if list_notes == []:
            print('\nВы не создали ни одной заметки.')
        else:
            next_pole = 'V'
            del_note = {}           # Временный словарь для хранения заметки для редактирования
            count_del = 0           # Счетчик совпадений
            choose_note = input(
                'Введите ID или имя пользователя или заголовок для редактирования заметки: ').capitalize()
            for i in range(len(list_notes)):
                for keys_00, value_00 in list_notes[i].items():
                    if value_00 == choose_note:         # Поиск совпадений
                        del_note = list_notes[i]        # Выбор нужной заметки
                        num = i                         # Номер выбранной заметки в списке словарей
                        count_del += 1                  # Количество заметок с одинаковым идентификатором
                print('')
            if count_del > 1:                           # Обнаружено больше одной заметки
                print(
                    f'Выявлено больше одного совпадения по метке {num_del}, введите другой идентификатор.')
            elif count_del == 0:                        # Заметок с таким запросом не обнаружено
                print('Заметок с таким ID или именем пользователя или заголовком не найдено.')
            else:
                # Цикл на изменение более одного поля в заметке, работает до ответа пользователя 'Нет'
                while next_pole != 'Нет':
                    temp_dict = del_note.copy()  # Создание копии на случай отмены редактирования
                    # Запуск функции редактирования заметки
                    list_notes[num] = upd_note(del_note)
                    # Запуск функции подтверждения изменения
                    conf_del_note = conf_change('изменить')
                    if conf_del_note == 'Нет':
                        # Восстановление заметки при отмене изменений
                        list_notes[num] = temp_dict
                    next_pole = input(
                        'Хотите отредактировать еще одно поле? Да/Нет ').capitalize()

    elif add_note == '4':           # Удаление заметки
        if list_notes == []:
            print('\nВы не создали ни одной заметки.')
        else:
            del_note = {}               # Временный словарь для хранение заметки на удаление
            count_del = 0               # Счетчик совпадений
            # Запрос по какому ID или имени или заголовку произвести удаление заметки
            num_del = input(
                'Введите ID или имя пользователя или заголовок для удаления заметки: ').capitalize()
            for i in range(len(list_notes)):
                for keys_00, value_00 in list_notes[i].items():
                    if value_00 == num_del:         # Поиск совпадений
                        del_note = list_notes[i]    # Выбор нужной заметки
                        count_del += 1              # Количество заметок с одинаковым идентификатором
                print('')
            if count_del > 1:                       # Обнаружено больше одной заметки
                print(
                    f'Выявлено больше одного совпадения по метке {num_del}, введите другой идентификатор.')
            elif count_del == 0:                    # Заметок с таким запросом не обнаружено
                print('Заметок с таким ID или именем пользователя или заголовком не найдено.')
            else:
                # Запуск функции подтверждения удаления
                conf_del_note = conf_change('удалить')
                if conf_del_note == 'Да':
                    list_notes.remove(del_note)     # Удаление заметки
                if conf_del_note == 'Нет':
                    print('Удаление отменено.')

    elif add_note == '5':                       # Поиск по заметкам по ключевому слову и/или статусу
        if list_notes == []:
            print('\nВы не создали ни одной заметки.')
        else:
            temp_dict = {}
            print('...Поиск...')
            search_keyword = input(
                'Введите ключевое слово для поиска или оставьте пустую строку: ').capitalize()
            search_status = input(
                'Введите строку статуса для поиска (или оставьте пустую строку): ').capitalize()
            # Проверка правильности ввода статуса
            while search_status not in ('Новая', 'В процессе', 'Выполнено', ''):
                search_status = input(
                    f'Выберите один из предложенных вариантов (Новая, В процессе, Выполнено): ').capitalize()

            if search_keyword == '' and search_status == '':            # Если задан пустой запрос в обоих строках
                print('Задан пустой поисковый запрос.')
            elif search_keyword != '' and search_status == '':          # Поиск если задано только ключевое слово
                # Вызов функции поиска заметок с объявлением именной переменной 'keyword='
                temp_dict = search_notes(list_notes, keyword=search_keyword)
            elif search_keyword == '' and search_status != '':          # Поиск если задан только статус
                # Вызов функции поиска заметок с объявлением именной переменной 'status='
                temp_dict = search_notes(list_notes, status=search_status)
            else:                                                       # Поиск по двум условиям
                temp_dict = search_notes(list_notes, search_keyword, search_status)

            for i in range(len(temp_dict)):
                # Вывод каждой заметки в виде словаря
                for keys_00, value_00 in temp_dict[i].items():
                    # Вывод данных ровными столбцами
                    print('{:<16} {:<15}'.format(keys_00, value_00))
                print('-------------------------')

    elif add_note == '6':
        # Команда 'Выход' Прерывание цикла
        print('\nУдачного дня.\n')
        making_note = False
    else:
        print('\nНеверный выбор. Пожалуйста, выберите действие из списка.')

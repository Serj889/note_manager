# Grade 1. Этап 2: Задание 3
# Задание: Обработка дедлайнов


from datetime import datetime       # Вызов библиотеки datetime

print('')
today = datetime.today().date()         # Запрос сегодняшней даты
print('Текущая дата:', today.strftime('%d-%m-%Y'))
print('')

# Запрос даты дедлайна
# Цикл проверки введенной даты требуемому формату
# Доступные форматы ввода: день-месяц-год или год-месяц-день
while True:
    issue_date = input(
        'Введите дату дедлайна (в формате день-месяц-год или год-месяц-день): ')
    try:
        user_date = datetime.strptime(issue_date, '%d-%m-%Y').date()
        break
    except ValueError:
        try:
            user_date = datetime.strptime(issue_date, '%Y-%m-%d').date()
            break
        except ValueError:
            print(
                'Убедитесь, что вводите дату в формате день-месяц-год или год-месяц-день, например: 01-12-2024.')
            print('')
            continue

# Вычисление дельты дней в значении по модулю
deadline_date = abs(user_date - today)

# Выбор корректного ответа в пределах одного месяца
# 5..20 25..30 - дней
# 2..4 22..24 - дня
# 1 21 31 - день
temp_date = int(deadline_date.days)
if (5 <= temp_date <= 20) or (25 <= temp_date <= 30):
    days = 'дней'
elif temp_date in (1, 21, 31):
    days = 'день'
else:
    days = 'дня'
print('')

# Ответ пользователю сколько дней
# прошло или осталось относительно даты дедлайна
if user_date > today:
    print(f'До дедлайна осталось {deadline_date.days} {days}.')
elif user_date < today:
    print(f'Внимание! Дедлайн истёк {deadline_date.days} {days} назад.')
elif user_date == today:
    print('Внимание! Дедлайн сегодня.')
print('')

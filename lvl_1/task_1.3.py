# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

from datetime import date, datetime
import calendar

now = datetime.now()
monthNow = now.strftime("%m")
monthNowWord = now.strftime("%B")
yearNow = now.strftime("%Y")

print(yearNow)
mnth = input('Введите номер месяца: ')

if 0 < int(mnth) < 13:
    print(f'Вы ввели {monthNowWord}. {calendar.monthrange(int(yearNow), int(mnth))[1]} дней' )
else:
    print('Такого месяца нет! Вы ввели: ' + mnth)

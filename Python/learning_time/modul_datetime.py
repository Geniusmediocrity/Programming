import datetime
from icecream import ic


#!               Модуль datetime
# Модуль datetime в Python предоставляет классы для работы с датой и временем,
# которые позволяют выполнять различные операции: 
#   сложение, вычитание, форматирование, сравнение и многое другое.
#? Основные классы модуля datetime:
#   date — для работы с датой (год, месяц, день).
#   time — для работы с временем (часы, минуты, секунды, микросекунды).
#   datetime — объединяет дату и время.
#   timedelta — используется для работы с временными интервалами.


#!                      datetime
#? Класс datetime объединяет в себе дату и время. Это самый универсальный класс для работы с временными объектами.
my_date = datetime.datetime(2025, 2, 12, 10, 42, 22)
ic(f"my_date = {my_date}")
print()

#? Основные методы класса datetime:
#   now() — возвращает текущие дату и время
now_date = datetime.datetime.now()
ic(f"Настоящая дата/время: {now_date}")
print()

#   now(timezone.utc) — возвращает текущие дату и время в формате UTC. 
# UTC (Coordinated Universal Time) — это всемирное координированное время,
# которое служит международным стандартом для определения времени. 
# Оно было введено в 1972 году и пришло на смену среднему времени по Гринвичу (GMT).
now_utc_date = datetime.datetime.now(datetime.timezone.utc)
ic(f"Таймзон utc: {now_utc_date}")
print()

#   fromtimestamp(timestamp) — возвращает объект datetime по Unix-времени
unix_date = datetime.datetime.fromtimestamp(123456789)
ic(f"Из unix в utc: {unix_date}")
print()

#   strftime(format) — форматирование даты и времени в строку
format_datetime = now_date.strftime("%Y--%m--%d %H.%M.%S")
ic(f"Форматированное время: {format_datetime}")
print()
#* Основные коды для форматирования:
#   %Y — полный год (например, 2024)
#   %m — месяц (01-12)
#   %d — день месяца (01-31)
#   %H — часы (00-23)
#   %M — минуты (00-59)
#   %S — секунды (00-59)
#   %A — полное название дня недели
#   %B — полное название месяца

#!                      date
#? Класс date используется для представления и работы с датой. 
#? Объект этого класса включает три поля: год, месяц и день.(year, manth, day)
my_date = datetime.date(1111, 11, 11)
ic(f"{my_date}")
print()

#? today() – возвращает текущую дату:
today_date = datetime.date.today()
ic(f"Дата сегодня: {today_date}")
print()

#? fromtimestamp(timestamp) – возвращает дату, соответствующую Unix-времени (количество секунд с начала эпохи Unix):
unix_date = datetime.date.fromtimestamp(123456789)
ic(f"Дата в формате Юникс(123456789): {unix_date}")
print()

#? replace(year, month, day) – возвращает новую дату с изменёнными значениями:
replace_date = my_date.replace(year=2222, day=22)
ic(f"Перестановленная my_date дата: {replace_date}")
print()

#? strftime(format) – форматирует дату в строку в соответствии с заданным форматом:
format_date = today_date.strftime("%d==%m==%Y")
ic(f"Форматирования дата сегодня: {format_date}")
print()

#? timetuple() – возвращает объект struct_time, аналогичный тому, что возвращает модуль time
time_tuple = today_date.timetuple()
ic(f"Это timetuple сегодняшнего дня: {time_tuple}")
print()


#!                   time
#? Класс time используется для работы с временем без даты.
#? Он может хранить часы, минуты, секунды и микросекунды.
my_time = datetime.time(10, 22, 33)
ic(f"datetime время: {my_time}")
print()

#? strftime(format) — форматирование времени в строку в соответствии с заданным форматом:
format_time = my_time.strftime("%H-%M-%S")
ic(f"Форматированная строка: {format_time}")
print()

#? replace(hour, minute, second, microsecond) — возвращает время с обновлёнными значениями
replace_time = my_time.replace(hour=20, minute=33, second=44)
ic(f"replaced time: {replace_time}\n")


#!                  timedelta
#? Класс timedelta используется для представления разницы между двумя временными объектами. 
#? Он позволяет выполнять арифметические операции над временными интервалами.
#? Основные атрибуты класса timedelta:
#   days
#   seconds
#   microseconds
#   milliseconds
#   minutes
#   hours
#   weeks
time_delta = datetime.timedelta(hours=999, minutes=20)
print(time_delta)
print(time_delta.days)
print()

#? Основные операции:
#   Сложение и вычитание:
start_time = datetime.datetime.now()
time_delta = datetime.timedelta(days=5, hours=5)
# Добавление временного интервала
new_date = start_time + time_delta
print(f"new addition date is: {new_date}")
# Вычитание временного интервала
new_date = start_time - time_delta
print(f"new substraction date is: {new_date}")
# Разница между датами:
dif_date = datetime.datetime(2000, 10, 13)
difference = start_time - dif_date
print(f"difference: {difference}")
# Умножение на число
double_delta = time_delta * 10
print(double_delta)

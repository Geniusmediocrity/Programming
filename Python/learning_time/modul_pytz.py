import pytz
import datetime

from icecream import ic


#!                  pytz
#? Модуль pytz в Python используется для работы с часовыми поясами.
# Он предоставляет поддержку для перевода между часовыми поясами и управления временем с учетом стандартного и летнего времени.

# Перед использованием модуля его необходимо установить (если он не установлен):

#? Особенности:
#   Часовые пояса и их объекты: Модуль pytz предоставляет доступ к временному стандарту и данным для большинства часовых поясов. Например, вы можете получить часовой пояс для Нью-Йорка, Лондона, Токио и многих других городов по их названиям.
#   Корректное преобразование времени: Благодаря pytz можно корректно преобразовывать время между часовыми поясами с учетом летнего времени (DST, Daylight Saving Time).


#? Получение доступных часовых поясов
# Список всех доступных часовых поясов:
timezones = pytz.all_timezones
print(len(timezones))   # Количество часовых поясов
ic(timezones)        # Примеры часовых поясов
print()


#? Работа с UTC
# Получение объекта часового пояса UTC:
timezones_utc = pytz.UTC
ic(timezones_utc)
print()

#? Получение локального времени в заданном часовом поясе
now = datetime.datetime.now()       # Текущее UTC время
timezone = pytz.timezone("Asia/Tokyo")    # Перевод в другой часовой пояс
localtime = timezone.localize(now)        # Перевод времени в указанный часовой пояс
print(localtime)
print()

#? Перевод между часовыми поясами:
now_utc = datetime.datetime.now(pytz.UTC)   # Текущее UTC время
moscow_tz = pytz.timezone("Europe/Moscow")
moscow_time = now_utc.astimezone(moscow_tz)
print(f"Now UTC time: {now_utc}")
print(f"Now Moscow time: {moscow_time}")
print()

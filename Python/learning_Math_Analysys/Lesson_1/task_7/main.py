import pandas as pd


pd.set_option("display.max_rows", 100)

df = pd.read_csv("Lesson_1/task_5/itresume-users-pandas.csv", delimiter=";", skiprows=1)
weekday_names = pd.to_datetime(df["date_joined"]).dt.day_name()
registrations_by_weekday = {}
for reg in weekday_names :
    registrations_by_weekday[reg] = registrations_by_weekday.get(reg, 0) + 1

registrations_by_weekday = dict(sorted(registrations_by_weekday.items(), key=lambda tup: tup[::-1], reverse=True))

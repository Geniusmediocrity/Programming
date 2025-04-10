import pandas as pd


df = pd.read_csv("Lesson_1/task_1/itresume-users-pandas.csv", delimiter=";", skiprows=1)

# Проверка корректности загрузки
print("Первые строки датафрейма:")
print(df.head())
print("\nИнформация о датафрейме:")
print(df.info())

# Сохранение последних 3 строк в df2
df2 = df.tail(3)

# Проверка результата
print("\nПоследние 3 строки датафрейма df2:")
print(df2)
import pandas as pd
from pathlib import Path


#! Некоторые дополнительные функции pandas для работы с файлами CSV
# Библиотека pandas предоставляет удобные инструменты для выбора, фильтрации, группировки
# и агрегации данных, что позволяет эффективно анализировать и манипулировать табличными данными.

data = Path("Pandas_csv_reading/data.csv").resolve()
new_file = Path("Pandas_csv_reading/new_file.csv").resolve()

#?  Слияние (merge) :
df_1 = pd.read_csv(data,
                   delimiter=",",
                   header=0,
                   index_col="ID",
                   na_values=["-", "N/A", "Н/Д"],
                   usecols=["Name", "Age", "ID"]
                   )
df_2 = pd.read_csv(new_file,
                   delimiter=",",
                   header=0,
                   index_col="ID",
                   na_values=["-", "N/A"],
                   usecols=["Date", "Name", "ID"],
                   )
merged = pd.merge(df_1, df_2, left_on=None, right_on=None, left_index=False, right_index=False)
print(merged)
print()

#?  Сортировка :
df = pd.read_csv(data,
                 delimiter=",",
                 index_col="ID",
                 header=0,
                 usecols=["ID", "Name", "Age"]
                 )
df_sorted = df.sort_values(by="Age", ascending=False, key=abs)   # ascending тоже самое что и reverse в sort/sorted
print(df_sorted)
print()

#? Удаление дубликатов :
df = pd.read_csv(data,
                 delimiter=",",
                 index_col="ID",
                 header=0,
                 usecols=["Age", "Name", "ID"]
                 )
df_nodublicates = df.drop_duplicates(subset="Name", keep="last", ignore_index=True) #? subset - то по какому столбцу(-ам) проверять
                                                                                    #? keep - вхождение повторяющегося жлемента,
                                                                                    #? ignore_index - игнорировать ли индексирование датафрейма
print(df_nodublicates)
print()
print()


#? 1. Выбор данных: Вы можете выбирать определенные столбцы или строки данных с помощью оператора [] или метода loc[] и iloc[]
print("1:")
df = pd.read_csv(data,
                 delimiter=",",
                # index=range(1-10),
                 index_col="ID",
                 header=0,
                 usecols=["Name", "Age", "ID"],
                 na_values=["-", "N/A"]
                 )
selected_cols = df[["Name"]]
print("1.1:")
print(selected_cols)
print()

print("1.2:")
# df.loc[]:
#? Основное назначение : Доступ к данным по меткам (именам) индексов и столбцов.
# Синтаксис : df.loc[строка_метка, столбец_метка]
# Особенности :
#   Включает конец диапазона (например, df.loc[1:3] включает строки с индексами 1, 2, 3).
#   Работает с условиями (булевыми масками).
#   Может использоваться для изменения данных.
#   Поддерживает булевы маски
#   Можно изменять данные
# Выбор определенных строк по метке индекса:
selected_cols = df.loc[4] # Включая строки с метками индекса от 1 до 5
print(selected_cols)
print()

print("1.3:")
# df.iloc[]:
#? Основное назначение : Доступ к данным по целочисленным позициям (индексам).
# Синтаксис : df.iloc[номер_строки, номер_столбца]
# Особенности :
#   Не включает конец диапазона (аналогично Python-срезам, например, df.iloc[1:3] включает строки 1 и 2).
#   Работает только с числовыми индексами (даже если индексы DataFrame — строки).
#   Не поддерживает булевые маски
#   Можно изменять данные
# Выбор определенных строк по позиции:
selected_cols = df.iloc[4]    # Включая строки с позициями от 1 до 4
print(selected_cols)
print()
print()


#? 2. Фильтрация данных: Вы можете фильтровать данные, используя условия.
dftypes = {"ID": int, "Name": str, "Age": int}
df = pd.read_csv(data,
                 delimiter=",",
                 dtype=dftypes,
                 index_col="ID",
                 header=0,
                 usecols=["Name", "Age", "ID"],
                 na_values=["-", "N/A"]
                 )
print("2.1:")
print(df[df["Age"] > 16])
print()

print("2.2:")
print(df[df["Name"] == "Alex"])
print()

print("2.3:")
print(df[(df["Age"] >= 16) & (df["Name"] == "Alex")])
print()
print()


#? 3. Группировка и агрегация данных: pandas позволяет группировать данные по значениям определенных столбцов 
# и применять агрегирующие функции к группам.
"""
Основная идея
Группировка происходит в три этапа:

Разделение (Split) : Данные разбиваются на группы на основе значений в столбце(ах).
Применение (Apply) : К каждой группе применяется функция (например, сумма, среднее).
Объединение (Combine) : Результаты объединяются в новый DataFrame.
"""

dict_data = {
    'Название': ['Ноутбук', 'Смартфон', 'Книга', 'Мышь', 'Флешка', 'Роман', 'Ноутбук'],
    'Категория': ['Техника', 'Техника', 'Книги', 'Техника', 'Техника', 'Книги', 'Техника'],
    'Цена': [500, 300, 20, 15, 10, 25, 555]
}
df = pd.DataFrame(dict_data)

"""
После группировки можно применять агрегатные функции:

sum() -- Сумма
mean() -- Среднее значение
count() -- Количество элементов
min() / max() -- Минимальное/максимальное значение
std() / var() -- Стандартное отклонение/дисперсия
agg([func1, func2]) -- Несколько функций сразу
"""

#? Группировка по 'Категория' и суммирование 'Цена':
# a) Группировка по одному столбцу
print("3.1:")
print(df.groupby('Категория')['Цена'].sum())
print()
print("3.2")
print(df.groupby("Категория")["Цена"].mean())
print()

# b) Группировка по нескольким столбцам
print("3.3:")
print(df.groupby(["Категория", "Название"])["Цена"].agg(["sum", "mean", "count"]))
print()

# c) Группировка с пользовательской функцией
print("3.4:")
print(df.groupby(df["Категория"].apply(max))["Цена"].mean())
print()
print()


#? 4. Добавление и удаление столбцов: Вы можете добавлять новые столбцы или удалять существующие.
dict_data = {
    'Название': ['Ноутбук', 'Смартфон', 'Книга', 'Мышь', 'Флешка', 'Роман', 'Ноутбук'],
    'Категория': ['Техника', 'Техника', 'Книги', 'Техника', 'Техника', 'Книги', 'Техника'],
    'Цена': [500, 300, 20, 15, 10, 25, 555]
}
df = pd.DataFrame(dict_data)
print("4.1:")
# Добавление нового столбца с вычисленными значениями:
# Используйте transform(), чтобы применить функцию к каждой группе и сохранить исходные размеры DataFrame:
df["Mean"] = df.groupby("Название")["Цена"].transform(lambda x: x.mean())
print(df)
print()

print("4.2:")
df.drop("Mean", axis=1, inplace=True)    # axis=1 указывает, что удаляем столбец, inplace=True для 
print(df)
print()

print("4.3:")
# Фильтрация групп с помощью filter() (например, оставить категории с суммой > 100):
filterd = df.groupby("Название").filter(lambda x: x["Цена"].mean() > 100)
print(filterd)
print()

print("4.4:")
# Используйте apply() для сложных операций:
hard_operation = df.groupby("Категория").apply(lambda el: len(el) >= 5)
print(hard_operation)
print()
print()


#? 5. Получение уникальных значений столбце DataFrame
df = pd.read_csv(data,
                 delimiter=",",
                 dtype=dftypes,
                 index_col="ID",
                 header=0,
                 usecols=["ID", "Name", "Age"],
                 na_values=["-", "N/A"]
                 )
print("5.1:")
print(df["Age"].unique())
print()
print("5.2:")
print(df["Name"].unique())  # numpy.ndarray -- многомерный однородный массив с заранее заданным количеством элементов
print()
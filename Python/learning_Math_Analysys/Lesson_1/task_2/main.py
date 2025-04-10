import pandas as pd


df = pd.read_csv("Lesson_1/task_1/itresume-users-pandas.csv", 
                 delimiter=";", 
                 skiprows=1)
params = {
    'Имена столбцов': df.columns.tolist(), #? преобразует в список
    "Размер": df.size,
    "Форма": df.shape
}
print(params)

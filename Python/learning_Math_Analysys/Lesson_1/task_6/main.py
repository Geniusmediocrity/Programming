import pandas as pd


pd.set_option("display.max_rows", 100)

df = pd.read_csv("Lesson_1/task_5/itresume-users-pandas.csv", delimiter=";", skiprows=1)
dates = pd.to_datetime(df["date_joined"]).dt.date.astype("str").unique().tolist()

print(dates)
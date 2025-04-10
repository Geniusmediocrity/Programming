import pandas as pd


pd.set_option("display.max_rows", 100)

df = pd.read_csv("Lesson_1/task_5/itresume-users-pandas.csv", delimiter=";", skiprows=1)
df = df.dropna()
df["username"] = df["username"].astype("O").replace(r"\$", "", regex=True)
print(df)

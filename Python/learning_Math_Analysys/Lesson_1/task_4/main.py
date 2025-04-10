import pandas as pd


df = pd.read_csv("Lesson_1/task_4/itresume-users-pandas.csv", delimiter=";", skiprows=1)
df = df.rename(columns={
    "id": "user_id",
    "date_joined": "created_at",
    "username": "login"
})
df = df.loc[: , ["user_id", "created_at", "login"]]

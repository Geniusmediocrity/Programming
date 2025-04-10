import pandas as pd


df = pd.read_csv("itresume-users-pandas.csv", delimiter=";", skiprows=1)
are_types_equal = df["username"].dtype == df["date_joined"].dtype
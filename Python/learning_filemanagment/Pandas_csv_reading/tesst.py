import pandas as pd


df = pd.read_csv("credit_train.csv",
                 header=0,
                 na_values=["NaN", "NA"],
                 usecols=["Annual Income", "Loan Status", "Years in current job",  "Monthly Debt"],
                 delimiter=","
                )
df = df.sort_values(by="Annual Income", ascending=False).head()
df.to_csv("result.csv", index=False)
print(df)
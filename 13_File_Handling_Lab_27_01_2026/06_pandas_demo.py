import pandas as pd

df = pd.read_excel("People.xlsx")

print(df.columns)
print(df["Age"])
print(df["Age"].sum())
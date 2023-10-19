import pandas as pd

df = pd.read_csv("qq_csv_lms.csv", delimiter=",", skipinitialspace=True, encoding="cp1251")
df.columns = [i.lower().replace(" ", "_") for i in df.columns]
df = df[sorted(["ингредиент_2", "ингредиент_1", "вес"])]
print(df.corr())

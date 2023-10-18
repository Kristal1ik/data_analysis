import pandas as pd

df = pd.read_csv("qq_csv_lms.csv", delimiter=",", skipinitialspace=True, encoding="cp1251")
df.columns = [i.lower().replace(" ", "_") for i in df.columns]
df["брак"] = df["брак"].apply(lambda x: "0" if x ==
                              "Брак" else "1")
df = df[sorted(["ингредиент_1", "брак"])].corr()
print(round(df["брак"].iloc[1], 4))



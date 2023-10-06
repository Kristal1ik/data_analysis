import pandas as pd

df = pd.read_csv("data.csv", delimiter=',', skipinitialspace=True, decimal=',')
df.columns = [i.lower().replace(" ", "_") for i in df.columns]
df["возраст"] = (round(df["возраст"])).astype(int)

print(df[["возраст", "путешествует_с_детьми"]].head(10))

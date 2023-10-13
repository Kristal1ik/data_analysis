import pandas as pd

df = pd.read_csv("data.csv", delimiter=",", skipinitialspace=True)
df.columns = [i.lower().replace(" ", "_") for i in df.columns]
df = df.groupby(["покупательская_активность"]).describe()["разность_выручки_тек_прошлый_месяц"].astype(int)
print(df)


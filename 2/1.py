import pandas as pd

df = pd.read_csv("data.csv", delimiter=",", skipinitialspace=True)
df.columns = [i.lower().replace(" ", "_") for i in df.columns]
print(df.describe(include="object").T)

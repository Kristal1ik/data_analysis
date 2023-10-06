import pandas as pd

df = pd.read_csv("data.csv", delimiter=';', skipinitialspace=True)
df = df.dropna()
print(type(df))
print(*df.shape)

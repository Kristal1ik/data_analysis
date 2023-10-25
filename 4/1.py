import math
import pandas as pd


df = pd.read_csv("data.csv", delimiter=';', decimal=",")
p = df["доля_ответов"].iloc[0]
n = df["число_опрошенных"].iloc[0]
z = df["доверительный_уровень"].iloc[0]
h = z * math.sqrt((p * (1 - p)) / n)
print(round((p - h) * 100, 2), round((p + h) * 100, 2))

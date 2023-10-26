import math
import pandas as pd

df = pd.read_csv("data2.csv", delimiter=';', decimal=",")
N = 1200
n = df[df["пробег"] > 140].size
n_ = (n * N) / (N + n - 1)
z = 1.96
p = n / df.size
h = z * math.sqrt((p * (1 - p)) / n_)
print(round((p - h) * 100, 2), round((p + h) * 100, 2))

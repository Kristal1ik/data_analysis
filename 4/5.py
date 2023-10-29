import math

import pandas as pd

df = pd.read_csv("data5.csv", delimiter=';', decimal=",")
z = 1.96
N = 8000
n = df.size
df = df[df["вес_шоколадки"] >= 100]["вес_шоколадки"]
p = df.size / n
n = df.size
n_ = round((n * N) / (n + N - 1))
h1 = (math.sqrt(z ** 2 * (p * (1 - p)) / n_))
h1_new = round(h1 / 5, 3)
n_new = ((z * (math.sqrt(p * (1 - p)))) / h1_new) ** 2
print(str(round(h1, 3)) + " , " + str(round((n_new * (1 - N)) / (n_new - N))))

import math

import pandas as pd

d = {"допустимая_ошибка": [], "размер_выборки": []}
z = 1.96
p = 0.5

for h in range(1, 10):
    d["допустимая_ошибка"].append(h)
    d["размер_выборки"].append(int((((z *
                                (math.sqrt(p * (1 - p)))) / (h / 100)) ** 2) + 0.00001))
print(pd.DataFrame(d))

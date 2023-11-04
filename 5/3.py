import pandas as pd
from scipy.stats import chi2_contingency

df = pd.read_csv("задача_3.csv", delimiter=";", skipinitialspace=True, encoding="cp1251", decimal=",")
lst = []
for i in df.columns[2:]:
    chi = chi2_contingency(pd.crosstab(df["вид_зондирования"], df[i]))[1]
    lst.append([i, round(chi, 4)])

lst = sorted(lst, key=lambda elem: elem[1])
lst = [['показатель', 'р-уровень']] + lst
print(lst)

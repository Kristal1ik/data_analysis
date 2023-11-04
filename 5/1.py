import pandas as pd
import scipy.stats
import operator

df = pd.read_csv("задачи_1_и_5.csv", delimiter=";", skipinitialspace=True, encoding="cp1251")
df_unique = df["регион"].unique()
# lst = [['регион', 'р-уровень']]
lst = []
for i in df_unique:
    lst.append([i, round(
        scipy.stats.mannwhitneyu(df[df["регион"] == i]["время_до"],
                                 df[df["регион"] == i]["время_после"])[1], 4)])

lst = sorted(lst, key=lambda elem: elem[1])
lst = [['регион', 'р-уровень']] + lst
print(lst)

import pandas as pd
from scipy.stats import pearsonr, spearmanr, shapiro

df = pd.read_csv("задача_4.csv", delimiter=";", skipinitialspace=True, encoding="cp1251", decimal=",")
lst = []
df = df[df["Группа"] == "Группа_1"]

for i in df.columns[1:]:
    for j in df.columns[1:]:
        if i == j:
            continue
        if (shapiro(df[i])[1] > 0.05) and (shapiro(df[j])[1] > 0.05):
            pir = pearsonr(df[i], df[j])
            if pir[1] < 0.05:
                lst.append([i, j, round(pir[0], 2), round(pir[1], 4), "Пирсон"])
        else:
            spir = spearmanr(df[i], df[j])
            if spir[1] < 0.05:
                lst.append([i, j, round(spir[0], 2),
                            round(spir[1], 4), "Спирман"])
lst = sorted(lst, key=lambda elem: elem[2], reverse=True)
lst = [['показатель 1', 'показатель 2', 'значение корреляции', 'р-уровень', 'метод корреляции']] + lst
print(lst)

import pandas as pd
from scipy.stats import mannwhitneyu, ttest_ind, shapiro

df = pd.read_csv("задача_2.csv", delimiter=";", skipinitialspace=True, encoding="cp1251", decimal=",")
lst = []

for i in df.columns[1:]:
    if ((shapiro(df[df["group"] == "group_1"][i])[1] > 0.05)
            and (shapiro(df[df["group"] == "group_2"][i])[1] > 0.05)):
        lst.append([i, round(ttest_ind(df[df["group"]
                                          == "group_1"][i], df[df["group"] == "group_2"][i])[1], 4), "Стьюдент"])
    else:
        lst.append([i, round(mannwhitneyu(df[df["group"]
                                             == "group_1"][i], df[df["group"] == "group_2"][i])[1], 4), "Манн-Уитни"])
lst = sorted(lst, key=lambda elem: elem[1])
lst = [['показатель', 'р-уровень', 'метод расчёта']] + lst
print(lst)

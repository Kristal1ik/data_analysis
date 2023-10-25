# import pandas as pd
# import scipy
#
# df = pd.read_csv("qq_csv_lms.csv", delimiter=",", skipinitialspace=True, encoding="cp1251")
# df.columns = [i.lower().replace(" ", "_") for i in df.columns]
# df = df[(df["ингредиент_1"] < 270) & (df["номер_смены"] == 2)]
# xi = scipy.stats.chi2_contingency(pd.crosstab(df["оператор_линии"], df["брак"]))
# kramer = (xi[0] / (len(df) * (min(pd.crosstab(df["оператор_линии"], df["брак"]).shape)
#                               - 1))) ** 0.5
# print(round(kramer, 4))
#
# n = int(input())
#
#
# ans = n // 3 * 2 + int(bool(n % 3))
# print(ans)
n = int(input())
k = int(input())
print(n // k + k - 1)

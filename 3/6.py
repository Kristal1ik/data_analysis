import pandas as pd
from numpy import sqrt
import scipy

df = pd.read_csv("qq_csv_lms.csv", delimiter=",", encoding="cp1251")
df.columns = [i.lower().replace(" ", "_") for i in df.columns]
df["ингредиент_кат"] = df["ингредиент_1"].apply(lambda x: "менее_270" if x <= 270 else "более_270")
xi = scipy.stats.chi2_contingency(pd.crosstab(df["ингредиент_кат"], df["брак"]))
kramer = sqrt(xi[0] / pd.crosstab(df["ингредиент_кат"], df["брак"]).sum().sum())
print(round(kramer, 4))

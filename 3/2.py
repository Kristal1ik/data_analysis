import numpy as np
import pandas as pd

df = pd.read_csv("qq3_csv_lms.csv", delimiter=",", skipinitialspace=True, encoding="cp1251")
df.columns = [i.lower().replace(" ", "_") for i in df.columns]
df = df.groupby(["key"]).sum().corr(method="spearman").applymap(lambda x: np.nan if abs(x) < 0.85 else x)
print(df)


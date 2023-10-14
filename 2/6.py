import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv", skipinitialspace=True, delimiter=",")
df.columns = [i.lower().replace(" ", "_") for i in df.columns]

df = df[
    df["популярная_категория"].isin(["Домашний текстиль", "Кухонная посуда", "Мелкая бытовая техника и"
                                                                             " электроника"])]
df = df.groupby(["покупательская_активность"]).describe()["разность_выручки_тек_прошлый_месяц"].astype(int)
print(df)

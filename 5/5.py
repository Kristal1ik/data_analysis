import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv("задачи_1_и_5.csv", delimiter=";", skipinitialspace=True, encoding="cp1251", decimal=",")
fig, axs = plt.subplots()
region = input()
df = df[df["регион"] == region]

sns.boxplot(data=df, orient="h")
plt.xlabel("время")
plt.savefig("target_5_5.png")

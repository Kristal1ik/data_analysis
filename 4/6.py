import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

s = input()
df = pd.read_csv("data6.csv", delimiter=",", skipinitialspace=True)
df.columns = [i.lower().replace(" ", "_") for i in df.columns]
df = df[df["покупательская_активность"] == s]

fig, axs = plt.subplots(1, 2, figsize=(9, 3))
sns.histplot(data=df, x="выручка_от_клиента_текущий_месяц", bins=30, kde=True, ax=axs[0])
axs[0].set_ylabel("")
axs[0].set_xlabel("")

sns.boxplot(data=df, y="выручка_от_клиента_текущий_месяц", ax=axs[1])
plt.suptitle("Гистограмма и ящик с усами для количественных данных")
axs[1].set_ylabel("")
axs[1].set_xlabel("")
plt.savefig("target_4_6.png")

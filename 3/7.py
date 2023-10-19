import pandas as pd
import matplotlib.pyplot as plt
import scipy
import seaborn as sns

s = input().lower().replace(" ", "_")

df = pd.read_csv("qq_csv_lms.csv", delimiter=",", encoding="cp1251")
df.columns = [i.lower().replace(" ", "_") for i in df.columns]

fig, axs = plt.subplots()
sns.scatterplot(data=df, x="вес", y=s, hue="оператор_линии")
plt.suptitle("Диаграмма рассеяния:\n Анализ зависимости между факторами.", y=1.01, size=16)

plt.savefig("target_3_7.png")

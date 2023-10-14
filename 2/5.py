import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv", delimiter=",", skipinitialspace=True)
s = input().lower().replace(" ", "_")
df.columns = [i.lower().replace(" ", "_") for i in df.columns]

fig, ax = plt.subplots()

ax.pie(df[s].value_counts(), labels=df[s].value_counts().index, autopct='%1.1f%%')
plt.savefig("target_2_5.png")

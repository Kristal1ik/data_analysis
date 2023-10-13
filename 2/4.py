import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv", delimiter=",", skipinitialspace=True)
s = input().lower().replace(" ", "_")
df.columns = [i.lower().replace(" ", "_") for i in df.columns]

fig, axs = plt.subplots()
sns.kdeplot(data=df, x=s, hue="покупательская_активность", fill=True)
plt.ylabel("")
plt.savefig("target_2_4.png")

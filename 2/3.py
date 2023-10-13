import matplotlib.pyplot as plt
import pandas as pd


s = input().lower().replace(" ", "_")
df = pd.read_csv("data.csv", delimiter=",", skipinitialspace=True)
df.columns = [i.lower().replace(" ", "_") for i in df.columns]

fig, axs = plt.subplots()
plt.grid(visible=None, which='major', axis='both')
axs.set_title(s)
axs.hist(df[s])
plt.savefig('target_2_3.png')
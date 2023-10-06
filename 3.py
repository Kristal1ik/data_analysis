import pandas as pd

df = pd.read_csv("data.csv", delimiter=',', skipinitialspace=True)
# skipinitialspace -- Skip spaces after delimiter.
df["возраст_кат"] = df["возраст"].map(lambda x: "менее_30" if int(x) <= 30 else "более_30")
# df.index.name = "возраст_кат"
print(round(df["возраст_кат"].value_counts(normalize=True) * 100).astype(int).to_frame())

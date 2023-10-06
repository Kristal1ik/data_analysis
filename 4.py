import pandas as pd

df = pd.read_csv("data.csv", delimiter=",")
df["расстояние_кат"] = df["расстояние"].map(
    lambda x: "домашний_регион" if int(x) <= 300 else "недалеко_отдома" if int(x) > 300 and int(
        x) <= 700 else "дальнее_путешествие")
print(round(df["расстояние_кат"].value_counts(normalize=True) * 100).astype(int).to_frame())

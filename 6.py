import pandas as pd


df = pd.read_csv("data.csv", delimiter=",", skipinitialspace=True)
df = df[df["общая_оценка_качества_предоставленной_услуги"] == "плохо"]
df["расстояние_кат"] = df["расстояние"].map(
    lambda x: "домашний_регион" if int(x) <= 300 else "не_так_далеко" if int(x) > 300 and int(
        x) <= 700 else "дальнее_путешествие")


print((round(df.groupby(["расстояние_кат"]).value_counts(
    ["путешествует_с_детьми"],
    normalize=True) * 100, 1).to_frame().sort_index()).rename(
    columns={"proportion": 0}))

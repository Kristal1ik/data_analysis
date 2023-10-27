import pandas as pd


df = pd.read_csv("data3.csv", delimiter=';', decimal=",")
df = df[df["название"] == "Полёт"]
df = df[(df["вес_шоколадки"] > df["вес_шоколадки"].quantile(0.01)) & (
        df["вес_шоколадки"] < df["вес_шоколадки"].quantile(0.99))]
h = 1
z = 1.96
sigma = df["вес_шоколадки"].var()
print(str(round(((z * sigma) / h) ** 2)) + ".0")

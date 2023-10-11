import pandas as pd


df = pd.read_csv("data.csv", delimiter=",", skipinitialspace=True)

n_yes = 0
n_no = 0


def n_yess(n):
    global n_yes, n_no
    if n:
        n_yes += 1
    else:
        n_no += 1


# n_yes_child = df[df["путешествует_с_детьми"] == "да"]
# n_no_child = df[df["путешествует_с_детьми"] == "нет"]
#
# n_yes_child.value_counts()
#
# ans = pd.concat([round(n_yes_child["общая_оценка_качества_предоставленной_услуги"].value_counts(normalize=True) * 100).to_frame(), round(n_no_child["общая_оценка_качества_предоставленной_услуги"].value_counts(normalize=True) * 100).to_frame()]).rename(
#     columns={"proportion": 0})
# middle = len(ans)
# print(middle)
# for i in ans.iterrows():
#     print(i)
# df["общая_оценка_качества_предоставленной_услуги1"] = df["общая_оценка_качества_предоставленной_услуги"]
print((round(df.groupby(["путешествует_с_детьми"]).value_counts(
    ["расстояние_кат"],
    normalize=True) * 100, 1).to_frame().sort_index()).rename(
    columns={"proportion": 0}))

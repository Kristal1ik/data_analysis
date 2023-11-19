# -*- coding: utf-8 -*-

import pandas as pd
import sklearn.model_selection
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import r2_score, mean_absolute_percentage_error
import numpy as np

df = pd.read_csv("tg_4_.csv", delimiter=";", skipinitialspace=True, encoding="cp1251", decimal=",")
df.dropna(inplace=True)
md = df.groupby(['порода'])['удой'].transform("median")

std = df['удой'].std() * 3
outliers = (df['удой'] - md).abs() > std
df.loc[outliers, "удой"] = np.nan
df['удой'].fillna(md, inplace=True)

df["порода"].replace("РефлешнСоверинггггг", "РефлешнСоверинг", inplace=True)
df["спо_кат"] = df["спо"].apply(lambda x: 1 if x <= 0.9 else 2)
df["порода"] = OneHotEncoder().fit_transform(df[["порода"]]).toarray()
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(df[["эке", "протеин", "спо_кат", "порода"]],
                                                                            df["удой"], random_state=42,
                                                                            test_size=0.15)
lr = LinearRegression().fit(X_train, y_train)
pred = lr.predict(X_test)
print(round(r2_score(y_test, pred), 2), round(mean_absolute_percentage_error(y_test, pred) * 100, 2))

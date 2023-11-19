# -*- coding: utf-8 -*-
import pandas as pd
import sklearn.model_selection
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import r2_score, mean_absolute_error

df = pd.read_csv("tg_3_.csv", delimiter=";", skipinitialspace=True, encoding="cp1251")
df["кузов"] = OneHotEncoder().fit_transform(df[["кузов"]]).toarray()
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(df[["кузов", "возраст", "мощность"]],
                                                                            df["цена"], random_state=42,
                                                                            test_size=0.15)
lr = LinearRegression().fit(X_train, y_train)
pred = lr.predict(X_test)
print(round(r2_score(y_test, pred), 2), round(mean_absolute_error(y_test, pred), 2))

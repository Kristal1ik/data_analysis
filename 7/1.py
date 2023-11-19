# -*- coding: utf-8 -*-
import pandas as pd
import sklearn.model_selection
from sklearn.linear_model import LinearRegression

df = pd.read_csv("tg_1_.csv", delimiter=";", skipinitialspace=True, encoding="cp1251")
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(df[["температура", "влажность"]],
                                                                            df["продажи"], random_state=42,
                                                                            test_size=0.15)

lr = LinearRegression().fit(X_train, y_train)
print(lr.predict(X_test).round())

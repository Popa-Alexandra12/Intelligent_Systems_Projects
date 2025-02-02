# -*- coding: utf-8 -*-
"""WineQuality.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O5Pywp1VXi9R9C52LwEOL_KLk5ro-xXG

# Selection of important features and predicting wine quality using machine learning techniques

## Imports
"""

import pandas as pd
import numpy as np
import sklearn 
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing  import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score
from sklearn.neural_network import MLPRegressor
from sklearn import svm

"""## Data preparation

### Reading dataset
"""

data_df = pd.read_csv("winequality-white.csv")
data_df

data_df.columns

data_df.head()

data_df.dtypes

"""## Cleaning dataset"""

data_df.describe(include="all")

"""## Split dataset"""

data_sel=data_df.copy()

y=data_df["quality"]
y_sel=data_sel["quality"]

data_df.drop(columns=["quality"],inplace=True)
data_sel.drop(columns=["quality"],inplace=True)

#noul dataset cu atributele mai semnificative selectate 
#atributele mai putin semnificative  sunt eliminate din datasetul compet
data_sel.drop(columns=["citric acid"],inplace=True)
data_sel.drop(columns=["chlorides"],inplace=True)
data_sel.drop(columns=["total sulfur dioxide"],inplace=True)

X=data_df
X_sel=data_sel

X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.20, random_state=42)
X_sel_train,X_sel_test,y_sel_train,y_sel_test=train_test_split(X_sel,y_sel, test_size=0.20, random_state=42)

X_train

X_sel_train

y_train

y_sel_train

"""## Machine Learning Alg."""

data_df.dtypes

data_sel.dtypes

all_features=["fixed acidity","volatile acidity","citric acid","residual sugar","chlorides","free sulfur dioxide","total sulfur dioxide","density","pH","sulphates","alcohol"]

sel_features=["fixed acidity","volatile acidity","residual sugar","free sulfur dioxide","density","pH","sulphates","alcohol"]

preprocessor = ColumnTransformer([     
    ("num", Pipeline([("scaler", StandardScaler())]), all_features)],     
    remainder="drop")

preprocessor_sel = ColumnTransformer([     
    ("num", Pipeline([("scaler", StandardScaler())]), sel_features)],     
    remainder="drop")

preprocessor.fit(X_train)
X_train=preprocessor.transform(X_train)

X_test=preprocessor.transform(X_test)

preprocessor_sel.fit(X_sel_train)
X_sel_train=preprocessor_sel.transform(X_sel_train)

X_sel_test=preprocessor_sel.transform(X_sel_test)

"""## Linear Regression"""

linreg=LinearRegression()
linreg.fit(X_train,y_train)

scores=cross_val_score(linreg,X_train,y_train,scoring="r2", cv=5)
np.mean(scores)

y_pred=linreg.predict(X_test)

r2_score(y_test,y_pred)

"""### Multi-Layer Perceptron

Rezultate obtinute pentru setul de date compet
"""

mlp = MLPRegressor(random_state=1, max_iter=1000,hidden_layer_sizes=(5))
mlp.fit(X_train, y_train)

scores=cross_val_score(mlp,X_train,y_train,scoring="r2", cv=5)
np.mean(scores)

y_pred=mlp.predict(X_test)

r2_score(y_test, y_pred)

"""Rezultate obtinute pentru setul cu date selectate"""

mlp_sel = MLPRegressor(random_state=1, max_iter=1000,hidden_layer_sizes=(5))
mlp_sel.fit(X_sel_train, y_sel_train)

scores=cross_val_score(mlp_sel,X_sel_train,y_sel_train,scoring="r2", cv=5)
np.mean(scores)

y_pred=mlp_sel.predict(X_sel_test)

r2_score(y_sel_test, y_pred)

"""# Support Vector Machine

Rezultate obtinute pentru setul de date compet
"""

regr = svm.SVR(kernel='linear',C=100)
regr.fit(X_train,y_train)

scores=cross_val_score(regr,X_train,y_train,scoring="r2", cv=5)
np.mean(scores)

y_pred=regr.predict(X_test)

r2_score(y_test, y_pred)

"""Rezultate obtinute pentru setul cu date selectate"""

regr_sel = svm.SVR(kernel='linear',C=100)
regr_sel.fit(X_sel_train,y_sel_train)

scores=cross_val_score(regr_sel,X_sel_train,y_sel_train,scoring="r2", cv=5)
np.mean(scores)

y_pred=regr_sel.predict(X_sel_test)

r2_score(y_sel_test, y_pred)
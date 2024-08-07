# -*- coding: utf-8 -*-
"""Project 4:House Predict.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14pwYSpQzIrB9ltIfrS4kcs9zC-8vQEi_
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics

sklearn.datasets.fetch_california_housing()

house_price_dataframe=pd.DataFrame(sklearn.datasets.fetch_california_housing().data,columns=sklearn.datasets.fetch_california_housing().feature_names)

house_price_dataframe.head()

house_price_dataframe.shape

house_price_dataframe.isnull().sum()

house_price_dataframe.describe()

correlation=house_price_dataframe.corr()

plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True,fmt='.1f', annot=True, annot_kws={'size':8}, cmap='Blues')

X= house_price_dataframe.drop(['MedInc'],axis=1)
Y=house_price_dataframe['MedInc']

print(X)
print(Y)

X_train, X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.2,random_state=2)

print(X.shape,X_train.shape,X_test.shape)

model = XGBRegressor()

model.fit(X_train,Y_train)

training_data_prediction=model.predict(X_train)

print(training_data_prediction)

score_1=metrics.r2_score(Y_train,training_data_prediction)



score_2=metrics.mean_absolute_error(Y_train,training_data_prediction)

print("R squared error : ", score_1)
print("Mean Absolute Error : ", score_2)

plt.scatter(Y_train,training_data_prediction)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual Prices vs Predicted Prices")
plt.show()

test_data_prediction=model.predict(X_test)

score_1=metrics.r2_score(Y_test,test_data_prediction)



score_2=metrics.mean_absolute_error(Y_test,test_data_prediction)

print("R squared error : ", score_1)
print("Mean Absolute Error : ", score_2)


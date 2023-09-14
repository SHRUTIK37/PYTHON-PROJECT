# -*- coding: utf-8 -*-
"""Ice Cream Sales Revenue Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16XRi28dcVwyjpE8jPabKUkfesVqi7kBd
"""

#Ice Cream Sales Revenue Prediction
# Step 1 : import library
import pandas as pd

# Step 2 : import data
icecream = pd.read_csv('https://github.com/ybifoundation/Dataset/raw/main/Ice%20Cream.csv')

# Step 3 : define target (y) and features (X)
icecream.columns

y = icecream['Revenue']
X = icecream[['Temperature']]

# Step 4 : train test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, train_size=0.7, random_state=2529)

# check shape of train and test sample
X_train.shape, X_test.shape, y_train.shape, y_test.shape

# Step 5 : select model
from sklearn.linear_model import LinearRegression
model = LinearRegression()

# Step 6 : train or fit model
model.fit(X_train,y_train)

model.intercept_

model.coef_

# Step 7 : predict model
y_pred = model.predict(X_test)



y_pred

# Step 8 : model accuracy
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error

mean_absolute_error(y_test,y_pred)

mean_absolute_percentage_error(y_test,y_pred)
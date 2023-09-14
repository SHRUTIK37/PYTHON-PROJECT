# -*- coding: utf-8 -*-
"""cancer prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ku_RTApDZZetoDmZZrXbybiQ7vtq2dYh
"""

#Cancer Prediction
# Step 1 : import library
import pandas as pd

# Step 2 : import data
cancer = pd.read_csv('https://github.com/YBIFoundation/Dataset/raw/main/Cancer.csv')

cancer.head()

cancer.info()

cancer.describe()

# Step 3 : define target (y) and features (X)
cancer.columns

y = cancer['diagnosis']
X = cancer.drop(['id','diagnosis','Unnamed: 32'],axis=1)

# Step 4 : train test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, train_size=0.7, random_state=2529)

# check shape of train and test sample
X_train.shape, X_test.shape, y_train.shape, y_test.shape

# Step 5 : select model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=5000)

# Step 6 : train or fit model
model.fit(X_train,y_train)

model.intercept_

model.coef_

# Step 7 : predict model
y_pred = model.predict(X_test)

y_pred

# Step 8 : model accuracy
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

confusion_matrix(y_test,y_pred)

accuracy_score(y_test,y_pred)

print(classification_report(y_test,y_pred))
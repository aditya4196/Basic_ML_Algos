# -*- coding: utf-8 -*-
"""LogisticRegression_Classifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B7Cv6kyGISYGdAKsg6RZUyi9Crb1pevF
"""

import sklearn
import pandas as pd

titanic_df = pd.read_csv('sample_data/titanic_train_processed.csv')

titanic_df.head()

titanic_df.shape

from sklearn.model_selection import train_test_split

X = titanic_df.drop('Survived', axis=1)
Y = titanic_df['Survived']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

x_train.shape, y_train.shape

x_test.shape, y_test.shape

from sklearn.linear_model import LogisticRegression

logistic_model = LogisticRegression(penalty = 'l2', C = 1.0, solver = 'liblinear').fit(x_train, y_train)

y_pred = logistic_model.predict(x_test)

pred_results = pd.DataFrame({'y_test' : y_test, 'y_pred' : y_pred})

pred_results.head()

titanic_crosstab = pd.crosstab(pred_results.y_pred, pred_results.y_test)

titanic_crosstab.head()

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

acc = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)

print("accuracy_score : ",acc)
print("recall score : ",recall)
print("precision_score : ",precision)










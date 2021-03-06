# -*- coding: utf-8 -*-
"""scikitlearnFirst.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O3s7S9IuWJJCGaQtrycu5SHT3rcQYVSE
"""

import sklearn

import numpy as np
import scipy as sp
import pandas as pd

from sklearn.datasets import load_breast_cancer

breast_cancer_dataset = load_breast_cancer()

print(breast_cancer_dataset.DESCR)

breast_cancer_dataset.keys()

breast_cancer_dataset.feature_names

breast_cancer_dataset.data.shape

breast_cancer_dataset.target_names

breast_cancer_dataset.target

df_features = pd.DataFrame(breast_cancer_dataset.data, columns=breast_cancer_dataset.feature_names)

df_targets = pd.DataFrame(breast_cancer_dataset.target, columns=['cancer'])

print(df_features)

df_targets.head

df = pd.concat([df_features, df_targets], axis=1)

df.head

df.head()

from sklearn.datasets import load_boston

boston_dataset = load_boston()

print(boston_dataset.DESCR)

df_boston_features = pd.DataFrame(boston_dataset.data,columns=boston_dataset.feature_names)



from google.colab import drive
drive.mount('/content/drive')

df_boston_features.head()



boston_dataset.data.shape












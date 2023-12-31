# -*- coding: utf-8 -*-
"""EDS Minor Project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bGFS-iDtvB4793abJGcHE9yHwJqFG8Wx

# **Minor Project**
We took the mill workers as our subject. Developed algorithmic model to decide the bonus salary he will get as per overtime hours that he devoted.
We used three method for the same:

Linear Regression, KNN and K-Means method.


**USING LINEAR REGRESSION**

Linear regression is a statistical modeling technique used to establish a relationship between a dependent variable and one or more independent variables. It assumes a linear relationship between the independent variables and the dependent variable.

The goal of linear regression is to find the best-fitting line that minimizes the differences between the observed data points and the predicted values on the line.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# To Load the dataset
dataset = pd.read_csv('mill_dataset.csv')
print(dataset.head())
print(dataset.describe())
# To Split the dataset into independent variable (X) and dependent variable (y)
X = dataset['overtime'].values.reshape(-1, 1)
y = dataset['bonus'].values
# Now Spliting the dataset into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# To Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)
# Predicting bonuses for the test set
y_pred = model.predict(X_test)
# Scatter plot data
plt.scatter(X_test, y_test, color='b', label='Actual')
plt.plot(X_test, y_pred, color='r', label='Predicted')
plt.xlabel('Overtime')
plt.ylabel('Bonus')
plt.title('Overtime vs Bonus')
plt.legend()
plt.show()

"""**USING KNN**

K-Nearest Neighbors (KNN) is a simple yet effective machine learning algorithm used for both classification and regression tasks. In KNN, the prediction for a new data point is based on the class or value of its nearest neighbors in the feature space.

It includes training, prediction, classification and regression.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
dataset = pd.read_csv('mill_dataset.csv')
print(dataset.head())
print(dataset.describe())
# Spliting the dataset in varisbles
X = dataset['overtime'].values.reshape(-1, 1)
y = dataset['bonus'].values

# Splitng the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Initialize and train the KNN classifier
k = 3
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train, y_train)

# Predicting
y_pred = model.predict(X_test)
# Calculating the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Ploting graphs of the actual data and predicted classes
plt.scatter(X_test, y_test, color='b', label='Actual')
plt.scatter(X_test, y_pred, color='r', label='Predicted')
plt.xlabel('Overtime')
plt.ylabel('Bonus')
plt.title('KNN Classification: Overtime vs Bonus')
plt.legend()
plt.show()

"""**USING K-Means**

K-Means is a popular unsupervised machine learning algorithm used for clustering data. It aims to partition a given dataset into distinct groups or clusters based on the similarity of data points. The algorithm works by iteratively assigning data points to the nearest cluster centroid and updating the centroids based on the mean values of the assigned data points.

It includes initialising, assigning centrioid, updating position of each, iterating and then final result.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load the dataset
dataset = pd.read_csv('mill_dataset.csv')
print(dataset.head())
print(dataset.describe())
# Selecting the features for clustering
X = dataset[['overtime', 'bonus']].values
# Initializing the K-Means model
k = 3
model = KMeans(n_clusters=k, random_state=42)
model.fit(X)
labels = model.labels_
# coordinates of the cluster centers
cluster_centers = model.cluster_centers_
# Ploting the data
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', marker='x')
plt.xlabel('Overtime')
plt.ylabel('Bonus')
plt.title('K-Means Clustering')
plt.show()
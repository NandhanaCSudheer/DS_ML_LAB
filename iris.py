from sklearn.datasets import load_iris

"""
sklearn → Scikit-learn, a popular Python library for machine learning.
datasets → a module inside Scikit-learn containing ready-made datasets.
load_iris → a function that loads the Iris dataset.
"""

iris = load_iris()

print(iris.data)

print(iris.data[0:5])

print(iris.target)

print(iris.target_names)

print(iris.feature_names)

print(len(iris.data))

print(len(iris.feature_names))

print(len(iris.target_names))

print(iris.data.shape)
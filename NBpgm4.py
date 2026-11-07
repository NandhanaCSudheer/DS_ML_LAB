# implement naive bayes classifier using scikit-learn

from sklearn import datasets
from sklearn import naive_bayes
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

X,y = iris.data,iris.target

classifier = naive_bayes.GaussianNB()

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.8)

classifier.fit(X_train,y_train)

result = classifier.predict(X_test)

accuracy = accuracy_score(y_test, result) * 100

print(f" Accuracy = {accuracy}")

features = [[int(i) for i in input(f"Enter {iris.feature_names}").split()]]

result = classifier.predict(features)

print(iris["target_names"][result]) 
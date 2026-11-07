# implement Decision Tree classifier using scikit-learn

from sklearn import datasets
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

iris = datasets.load_iris()

X,y = iris.data,iris.target

classifier = tree.DecisionTreeClassifier()     #  Creates a Decision Tree classification model.

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.7)

classifier.fit(X_train,y_train)

tree.plot_tree(classifier)    #  creates a graphical representation of the Decision Tree.

result = classifier.predict(X_test)

accuracy = accuracy_score(y_test, result) * 100

print(f" Accuracy = {accuracy}")

features = [[int(i) for i in input(f"Enter {iris.feature_names}").split()]]

result = classifier.predict(features)[0]

print(iris["target_names"][result])   #   Converting the number to the flower name

fig = plt.figure(figsize = (25,20))
_ = tree.plot_tree(classifier, feature_names = iris.feature_names, class_names = iris.target_names, filled = True)
plt.show()
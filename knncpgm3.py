import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import neighbors

iris = load_iris()
X = iris.data
y = iris.target

#Create knn classifier
knn = neighbors.KNeighborsClassifier(n_neighbors=3)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

knn.fit(X_train,y_train)  # trains the knn model

y_pred = knn.predict(X_test)

print("Precited values: ")
print(y_pred)
print("Actual values: ")
print(y_test)

# calculates accuracy
accuracy = accuracy_score(y_test,y_pred)
print("Accuracy score: ",accuracy)

#predict a new sample, format ->  [sepal lenght, sepal width, petal length, petal width]
sample = np.array([[5.9,3.0,5.1,1.8]])
pred = knn.predict(sample)
print("Predicted class = ",iris.target_names[pred][0])
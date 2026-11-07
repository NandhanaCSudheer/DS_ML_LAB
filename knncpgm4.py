# program to predict diabetes using knn classification

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import neighbors

diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

print(diabetes.data.shape)
print(diabetes.target.shape)
print(diabetes.feature_names)
print(diabetes.target)
print(diabetes.data[0])

knn = neighbors.KNeighborsClassifier(n_neighbors=3)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)

print("Precited values: ")
print(y_pred)
print("Actual values: ")
print(y_test)

accuracy = accuracy_score(y_test,y_pred)
print("Accuracy score: ",accuracy)


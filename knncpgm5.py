from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data
y = iris.target

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.25,random_state = 42)

model = KNeighborsClassifier(n_neighbors = 5)

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print("Accuracy = ",metrics.accuracy_score(y_test,y_pred))

sample = [[2,2,2,2]]
pred = model.predict(sample)[0]    # getting first prediction as the index of the flower type
print("New sample belongs to: ",iris.target_names[pred])

plt.subplot(1,2,1)
plt.scatter(X_test[:,0],X_test[:,1],c = y_pred)
plt.title("Predicted Class")
plt.xlabel("Petal length")
plt.ylabel("Petal width")
plt.subplot(1,2,2)
plt.scatter(X_test[:,0],X_test[:,1],c = y_test)
plt.title("Actual Class")
plt.xlabel("Petal length")
plt.ylabel("Petal width")
plt.show()
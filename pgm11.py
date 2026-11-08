from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score,root_mean_squared_error
import matplotlib.pyplot as plt

data = load_diabetes()
X = data.data
y = data.target

knn = KNeighborsRegressor(n_neighbors=3)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)
print("Mean Squared Error: ",mean_squared_error(y_test,y_pred))
print("R2 Score: ",r2_score(y_test,y_pred))
print("Mean Absolute error: ",mean_absolute_error(y_test,y_pred))
print("Root Mean Squared error: ",root_mean_squared_error(y_test,y_pred))
print()
sample = [[12.2,1.1,6.7,3.4,5.5,6.7,7.8,4.5,9.6,1.3]]
pred = knn.predict(sample)[0]
print(pred)

plt.scatter(range(len(y_test)),y_test,color = "red",label = "Actual output",marker = ".")
plt.scatter(range(len(y_pred)),y_pred,color = "blue",label = "Predicted Output",marker = "x")
plt.xlabel("Test sample")
plt.ylabel("Diabetes progression")
plt.legend()
plt.show()

plt.subplot(1,2,1)
plt.scatter(X_test[:,0],X_test[:,1],c = y_pred, label = "Actual")
plt.title("Predicted Class")
plt.xlabel("Petal length")
plt.ylabel("Petal width")
plt.subplot(1,2,2)
plt.scatter(X_test[:,0],X_test[:,1],c = y_test, label = "Predicted")
plt.title("Actual Class")
plt.xlabel("Petal length")
plt.ylabel("Petal width")
plt.show()
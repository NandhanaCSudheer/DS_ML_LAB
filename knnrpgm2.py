# program to predict diabetes using KNN regression. Values in the input features range approximately from -0.2 to +0.2

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import neighbors

diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

print("Data shape: ",diabetes.data.shape)
print("Target shape: ",diabetes.target.shape)
print("Feature names: ",diabetes.feature_names)
print("Target values: ")
print(diabetes.target)
print("First sample data: ")
print(diabetes.data[0])

knn = neighbors.KNeighborsRegressor(n_neighbors=5)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

knn.fit(X_train,y_train)

y_pred = knn.predict(X_test)

print("Precited values: ")
print(y_pred)
print("Actual values: ")
print(y_test)

mse = mean_squared_error(y_test,y_pred)
print("\nMean Squared Error: ",mse)

r2 = r2_score(y_test,y_pred)
print("\nR2 Score: ",r2)
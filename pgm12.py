from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score,root_mean_squared_error
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("pgm12.csv")
X = data[["Area","Bedrooms"]]
y = data["Price"]

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

knn = KNeighborsRegressor(n_neighbors=1)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)

print("Mean Squared Error: ",mean_squared_error(y_test,y_pred))
print("R2 Score: ",r2_score(y_test,y_pred))
print("Mean Absolute error: ",mean_absolute_error(y_test,y_pred))
print("Root Mean Squared error: ",root_mean_squared_error(y_test,y_pred))
print()
sample = pd.DataFrame({"Area":[3100],"Bedrooms":[5]})
sample_scaled = scaler.transform(sample)
pred = knn.predict(sample_scaled)
print(pred[0])

plt.scatter(range(len(y_test)),y_test,color = "red",label = "Actual output",marker = ".")
plt.scatter(range(len(y_pred)),y_pred,color = "blue",label = "Predicted Output",marker = "x")
plt.xlabel("Test sample")
plt.ylabel("House price prediction")
plt.legend()
plt.show()

plt.subplot(1,2,1)
plt.scatter(data["Area"],data["Bedrooms"],color = "red", marker = "*")
plt.title("Predicted Class")
plt.xlabel("Area")
plt.ylabel("Bedrooms")
plt.subplot(1,2,2)
plt.scatter(data["Area"],data["Bedrooms"],color = "blue", marker = "^")
plt.title("Actual Class")
plt.xlabel("Area")
plt.ylabel("Bedrooms")
plt.show()

plt.subplot(1,2,1)
plt.scatter(X_test[:,0],X_test[:,1],c = pd.factorize(y_pred)[0],cmap = "coolwarm", marker = "*")
plt.title("Predicted Class")
plt.xlabel("Area")
plt.ylabel("Bedrooms")
plt.subplot(1,2,2)
plt.scatter(X_test[:,0],X_test[:,1],c = pd.factorize(y_test)[0],cmap = "coolwarm", marker = "^")
plt.title("Actual Class")
plt.xlabel("Area")
plt.ylabel("Bedrooms")
plt.show()

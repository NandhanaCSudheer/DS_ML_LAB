
# import matplotlib.pyplot as plt
# import numpy as np
# from sklearn import datasets, linear_model
# from sklearn.metrics import mean_squared_error, r2_score

# X, y = datasets.load_diabetes(return_X_y=True)
# X = X[:, np.newaxis, 2]

# X_train, X_test = X[:-20], X[-20:]
# y_train, y_test = y[:-20], y[-20:]

# model = linear_model.LinearRegression()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)

# print("Coefficients:", model.coef_)
# print("Intercept:", model.intercept_)
# print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
# print("R^2 score: %.2f" % r2_score(y_test, y_pred))

# idx = np.argsort(X_test[:, 0])
# plt.scatter(X_test, y_test, color="black")
# plt.plot(X_test[idx], y_pred[idx], color="blue", linewidth=3)
# plt.xlabel("BMI")
# plt.ylabel("Diabetes progression")
# plt.title("Linear Regression: BMI vs Diabetes Progression")
# plt.xticks(fontsize=10)
# plt.yticks(fontsize=10)
# plt.show()



import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv("new.csv")

X = data[["study_hours"]]
y = data["result"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)
print("Mean squared error:", mean_squared_error(y_test, y_pred))
print("R2 score:", r2_score(y_test, y_pred))

plt.scatter(X_test, y_test, color="black")
idx = X_test["study_hours"].argsort()
plt.plot(X_test["study_hours"].iloc[idx], y_pred[idx], color="blue")
plt.xlabel("Study Hours")
plt.ylabel("Result")
plt.title("Linear Regression")
plt.show()

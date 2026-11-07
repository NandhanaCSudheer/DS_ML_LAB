
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv("new.csv")
X = data[["study_hours", "attendance"]]
y = data["result"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Mean squared error:", mean_squared_error(y_test, y_pred))
print("R2 score:", r2_score(y_test, y_pred))

plt.figure(figsize=(14, 5))

for i, color in enumerate(["blue", "green"]):
    plt.subplot(1, 2, i + 1)
    plt.scatter(X_test.iloc[:, i], y_test, color="red", label="Actual")
    plt.scatter(X_test.iloc[:, i], y_pred, color=color, marker="^", label="Predicted")
    plt.xlabel(X.columns[i])
    plt.ylabel("Result")
    plt.title(X.columns[i] + " vs Result")
    plt.legend()

plt.tight_layout()
plt.show()

plt.scatter(y_test, y_pred, color="purple", marker="^")
plt.plot([0, 1], [0, 1], "r--", label="Ideal Fit")
plt.xlabel("Actual Result")
plt.ylabel("Predicted Result")
plt.title("Actual vs Predicted")
plt.legend()
plt.show()

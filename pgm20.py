import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Create dataset
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [15, 20, 30, 35, 45, 50, 60, 65, 75, 85]
}

df = pd.DataFrame(data)

# Separate variables
X = df[["Study_Hours"]]
y = df["Marks"]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict marks
sample = pd.DataFrame({"Study_Hours": [7]})
pred = model.predict(sample)

print("Predicted Marks:", pred[0])

# Regression equation
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Regression Equation: y =", model.coef_[0],
      "* x +", model.intercept_)

# Accuracy
y_pred = model.predict(X)
print("R2 Score:", r2_score(y, y_pred))

# Visualization
plt.scatter(X, y, color="blue", label="Actual")
plt.plot(X, y_pred, color="red", label="Regression Line")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.legend()
plt.show()
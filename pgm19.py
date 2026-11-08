import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Load dataset
data = pd.read_csv("pgm19.csv")

# Separate variables
X = data[["YearsExperience"]]
y = data["Salary"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Best fit line
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Linear Equation is: ")
print(f"y = {model.coef_[0]:.2f}x + {model.intercept_}")

# Predict salary for new experience
sample = pd.DataFrame({"YearsExperience": [5]})
pred = model.predict(sample)
print("Predicted Salary:", pred[0])

# Evaluation
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R2 Score:", r2_score(y_test, y_pred))

# Visualization
plt.scatter(X_test, y_test, color="blue", label="Actual")
plt.scatter(X_test, y_pred, color="red", label="Predicted")
plt.plot(X_test, y_pred, color="green", label="Best Fit Line")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.show()
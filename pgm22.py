import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# Create dataset
data = {
    "Area": [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800],
    "Bedrooms": [2, 2, 3, 3, 4, 4, 4, 5],
    "Bathrooms": [1, 2, 2, 2, 3, 3, 3, 4],
    "Age": [10, 8, 5, 7, 4, 3, 2, 1],
    "Price": [30, 40, 55, 60, 75, 85, 100, 120]
}

df = pd.DataFrame(data)

# Independent variables
X = df[["Area", "Bedrooms", "Bathrooms", "Age"]]

# Dependent variable
y = df["Price"]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict new house price
sample = pd.DataFrame({
    "Area": [1600],
    "Bedrooms": [3],
    "Bathrooms": [2],
    "Age": [5]
})

pred = model.predict(sample)
print("Predicted House Price:", pred[0], "Lakhs")

# Display coefficients
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# Predict existing data
y_pred = model.predict(X)

# Evaluation
print("R2 Score:", r2_score(y, y_pred))
print("MSE:", mean_squared_error(y, y_pred))

# Visualization
plt.scatter(y, y_pred, color="blue")
plt.xlabel("Actual House Prices")
plt.ylabel("Predicted House Prices")
plt.title("Actual vs Predicted House Prices")
plt.show()
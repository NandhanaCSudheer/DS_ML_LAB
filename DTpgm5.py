import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Read JSON file
data = pd.read_json("new.json")

# Separate features and target
X = data[["study_hours", "attendance"]]
y = data["result"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy =", accuracy_score(y_test, y_pred) * 100)

# Predict new student
student = [[4, 70]]

prediction = model.predict(student)

if prediction[0] == 1:
    print("Pass")
else:
    print("Fail")
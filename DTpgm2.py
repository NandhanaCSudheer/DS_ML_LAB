
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("new.csv")

X = data[["study_hours", "attendance"]]
y = data["result"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

clsr = tree.DecisionTreeClassifier(random_state=42)
clsr.fit(X_train, y_train)

# Evaluate the model
y_pred = clsr.predict(X_test)

print("Accuracy score:", accuracy_score(y_test, y_pred))
print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification report:\n", classification_report(y_test, y_pred))

# Get input from the user
study_hours = int(input("Enter study hours: "))
attendance = int(input("Enter attendance: "))

sample = pd.DataFrame({
    "study_hours": [study_hours],
    "attendance": [attendance]
})

y2 = clsr.predict(sample)[0]

if y2 == 1:
    print("Result: Pass")
else:
    print("Result: Fail")

# Visualize the decision tree
plt.figure(figsize=(15, 8))
tree.plot_tree(
    clsr,
    feature_names=["study_hours", "attendance"],
    class_names=["Fail", "Pass"],
    filled=True
)
plt.show()

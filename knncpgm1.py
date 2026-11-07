import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import accuracy_score 
X = np.array([ [2,50], [3,55], [4,60], [5,65], [6,70], [7,75], [8,80], [9,85], [10,90], [11,95], [12,80], [13,85], [14,70], [15,65]]) 
y = np.array([0,0,0,0,0,1,1,1,1,1,1,1,1,1]) 
df = pd.DataFrame(X, columns=["Hours_Studied", "Attendance"]) 
print(df) 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 
knn = KNeighborsClassifier(n_neighbors=3) 
knn.fit(X_train, y_train) 
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred) 
print("Accuracy =", accuracy * 100, "%") 
new_data = np.array([[12, 80]]) 
prediction = knn.predict(new_data) 
if prediction[0] == 1: 
    print("Prediction: PASS") 
else: 
    print("Prediction: FAIL") 
k_values = range(1, 8) 
accuracies = [] 
for value in k_values: 
    model = KNeighborsClassifier(n_neighbors=value) 
    model.fit(X_train, y_train) 
    pred = model.predict(X_test) 
    acc = accuracy_score(y_test, pred) * 100 
    accuracies.append(acc) 
plt.plot(k_values, accuracies, marker="o") 
plt.xlabel("K Value") 
plt.ylabel("Accuracy (%)") 
plt.title("KNN Accuracy Graph") 
plt.xticks(k_values) 
plt.show() 
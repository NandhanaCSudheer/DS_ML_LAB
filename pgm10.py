from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("pgm10.csv")
X = data[["Study_hours","attendance_percentage"]]
y = data["result"]

knn = KNeighborsClassifier(n_neighbors=3)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)
print("Accuracy = ",accuracy_score(y_test,y_pred)*100)
print("Accuracy score: ",accuracy_score(y_test,y_pred))
print("Confusion matrix: ",confusion_matrix(y_test,y_pred))
print("Classification report: ",classification_report(y_test,y_pred))

# s1 = [[3,45]]
# s2 = [[10,60]]
# s3 = [[5,76]]
s1 = pd.DataFrame({"Study_hours":[3],"attendance_percentage":[45]})
s2 = pd.DataFrame({"Study_hours":[10],"attendance_percentage":[60]})
s3 = pd.DataFrame({"Study_hours":[5],"attendance_percentage":[76]})


y1 = knn.predict(s1)[0]
y2 = knn.predict(s2)[0]
y3 = knn.predict(s3)[0]
print(y1)
print(y2)
print(y3)

plt.scatter(range(len(y_test)),y_test,color = "red",label = "Actual output",marker = "^")
plt.scatter(range(len(y_pred)),y_pred,color = "blue",label = "Predicted output",marker = ".")
plt.xlabel("Test sample")
plt.ylabel("Output")
plt.title("Actual vs predicted")
plt.legend()
plt.show()

plt.subplot(1,2,1)
plt.scatter(data["Study_hours"],data["attendance_percentage"],color = "red", marker = "*")
plt.title("Predicted Class")
plt.xlabel("Study Hours")
plt.ylabel("Attendance Percentage")
plt.subplot(1,2,2)
plt.scatter(data["Study_hours"],data["attendance_percentage"],color = "blue", marker = "^")
plt.title("Actual Class")
plt.xlabel("Study Hours")
plt.ylabel("Attendance Percentage")
plt.show()

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
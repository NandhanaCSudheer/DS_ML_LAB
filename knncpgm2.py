from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import numpy as np
import pandas as pd

data = pd.read_csv("new.csv")
X = data[["study_hours","attendance"]]
y = data["result"]

knn = KNeighborsClassifier(n_neighbors=3)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)
print("Accuracy score: ",accuracy_score(y_test,y_pred))
print()
print("Confusion matrix: ",confusion_matrix(y_test,y_pred))
print()
print("Classification report: ",classification_report(y_test,y_pred))
print()


samples = pd.DataFrame({
    "study_hours": [10, 11, 12],
    "attendance": [73, 42, 97]
})

y1 = knn.predict(samples)


if y1[0] == 1:
    print("result = Pass")
else:
    print("Result = Fail")

if y1[1] == 1:
    print("result = Pass")
else:
    print("Result = Fail")

if y1[2] == 1:
    print("result = Pass")
else:
    print("Result = Fail")

# for i in range(len(y1)):
#     if y1[i] == 1:
#         print(f"Student {i+1}: Pass")
#     else:
#         print(f"Student {i+1}: Fail")
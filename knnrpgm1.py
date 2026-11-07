from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error,r2_score
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("new.csv")
X = data[["study_hours","attendance"]]
y = data["result"]

knn = KNeighborsRegressor(n_neighbors=3)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)
print("Mean Squared Error: ",mean_squared_error(y_test,y_pred))
print()
print("R2 Score: ",r2_score(y_test,y_pred))
print()

# sample = np.array([[10,73]])
# s2 = np.array([[11,42]])
# s3 = np.array([[12,97]])

samples = pd.DataFrame({
    "study_hours": [10, 11, 12],
    "attendance": [73, 42, 97]
})

y1 = knn.predict(samples)


# print(y1[0])
# print(y1[1])
# print(y1[2])

# for i, prediction in enumerate(y1):
#     print(f"Student {i+1}: Predicted result = {prediction:.2f}")

for i in range(len(y1)):
    if y1[i] == 1:
        print(f"Student {i+1}: Pass, {y1[i]}")
    else:
        print(f"Student {i+1}: Fail, {y1[i]}")
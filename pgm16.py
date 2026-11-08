from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("pgm16.csv")
X = data[["Weather","Temperature","Humidity"]]
y = data["Play_Cricket"]
X = pd.get_dummies(X, columns=["Weather"], dtype=int)

model = GaussianNB()

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.6,random_state=42)
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)
print("Accuracy = ",accuracy_score(y_test,y_pred)*100)
print("Accuracy score: ",accuracy_score(y_test,y_pred))
print("Confusion matrix: ",confusion_matrix(y_test,y_pred))
print("Classification report: ",classification_report(y_test,y_pred))

sample = pd.DataFrame({"Weather":["Cloudy"],"Temperature":[21],"Humidity":[62]})
sample = pd.get_dummies(sample, columns=["Weather"], dtype=int)
sample = sample.reindex(columns=X.columns, fill_value=0)
pred = model.predict(sample)
print(pred[0])

plt.scatter(range(len(y_test)),y_test,color = "red", marker = "*", label = "Actual output")
plt.scatter(range(len(y_pred)),y_pred,color = "blue", marker = "^", label = "Predicted output")
plt.legend()
plt.title("Actual vs Predicted")
plt.show()

plt.bar(["Naive Bayes"], [accuracy * 100]) 
plt.ylim(0, 100) 
plt.ylabel("Accuracy (%)") 
plt.title("Naive Bayes Accuracy") 
plt.show()

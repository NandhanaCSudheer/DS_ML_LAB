from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.naive_bayes import GaussianNB 
from sklearn.metrics import accuracy_score, confusion_matrix 
import matplotlib.pyplot as plt 

iris = load_iris() 
X, y = iris.data, iris.target 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 
model = GaussianNB() 
model.fit(X_train, y_train) 
y_pred = model.predict(X_test) 
accuracy = accuracy_score(y_test, y_pred) 
print("Accuracy:", accuracy) 
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred)) 
flower = [[5.1, 3.5, 1.4, 0.2]] 
prediction = model.predict(flower) 
print("Prediction:", iris.target_names[prediction[0]]) 
plt.bar(["Naive Bayes"], [accuracy * 100]) 
plt.ylim(0, 100) 
plt.ylabel("Accuracy (%)") 
plt.title("Naive Bayes Accuracy") 
plt.show() 
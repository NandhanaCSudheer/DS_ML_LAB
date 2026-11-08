from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import matplotlib.pyplot as plt

data = load_iris()
X = data.data
y = data.target

knn = GaussianNB()
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)
print("Accuracy = ",accuracy_score(y_test,y_pred)*100)
print("Accuracy score: ",accuracy_score(y_test,y_pred))
print("Confusion matrix: ",confusion_matrix(y_test,y_pred))
print("Classification report: ",classification_report(y_test,y_pred))
sample = [[12.2,1.1,6.7,3.4]]
pred = knn.predict(sample)[0]
print(pred)
print(data.target_names[pred])

plt.scatter(range(len(y_test)),y_test,color = "red",label = "Actual output",marker = ".")
plt.scatter(range(len(y_pred)),y_pred,color = "blue",label = "Predicted Output",marker = "x")
plt.xlabel("Test sample")
plt.ylabel("Flower features")
plt.legend()
plt.show()

# plt.subplot(1,2,1)
# plt.scatter(X_test[:,0],X_test[:,1],c = y_pred)
# plt.title("Predicted Class")
# plt.xlabel("Petal length")
# plt.ylabel("Petal width")
# plt.subplot(1,2,2)
# plt.scatter(X_test[:,0],X_test[:,1],c = y_test)
# plt.title("Actual Class")
# plt.xlabel("Petal length")
# plt.ylabel("Petal width")
# plt.show()

plt.bar(["Naive Bayes"], [accuracy * 100]) 
plt.ylim(0, 100) 
plt.ylabel("Accuracy (%)") 
plt.title("Naive Bayes Accuracy") 
plt.show()
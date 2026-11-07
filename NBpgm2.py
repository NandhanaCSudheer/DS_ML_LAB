from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB    # GaussianNB is a Naive Bayes machine-learning algorithm.
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target

#test_size=0.2 -  Use 20% of the data for testing and 80% for training.
#random_state=42 - Controls the random splitting.
#Using 42 means you will get the same split every time you run the program.
#The number 42 itself has no special meaning here; it is simply a commonly used fixed value.

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)  

model = GaussianNB()      #  Creates a Gaussian Naive Bayes classifier.

model.fit(X_train,y_train)     #   machine-learning model learns from the training data.

y_pred = model.predict(X_test)

print(y_pred)
print(y_test)

print(accuracy_score(y_test,y_pred))      # Calculates the percentage of correct predictions
print(confusion_matrix(y_test,y_pred))       #Shows how many samples were correctly/incorrectly classified for each class.
print(classification_report(y_test,y_pred))     # Provides Precision, Recall, F1-score, Support

#Precision  -  Of the samples predicted as a particular class, how many were actually that class?
#Recall  -  Of the samples actually belonging to a particular class, how many did the model correctly identify?
#F1-score  -  A combined measure of precision and recall.
#Support  -  Number of actual samples belonging to each class.

sample = np.array([[5.1,3.5,1.4,0.2]])
s2 = np.array([[3.14,9.8,6.02,2.414]])
s3 = np.array([[1.91,5.8,2.80,1.12]])

pred = model.predict(sample)
pred2 = model.predict(s2)
pred3 = model.predict(s3)

print("Predicted class = ",pred)
print("Predicted class = ",pred2)
print("Predicted class = ",pred3)
print(iris.target_names[pred])
print(iris.target_names[pred2])
print(iris.target_names[pred3])
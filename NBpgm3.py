# implement guassian using the public dataset load_breast_cancer

from sklearn.datasets import load_breast_cancer    #  measurements of breast cancer tumors and a target indicating the diagnosis category.
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

data = load_breast_cancer()
X = data.data
y = data.target

print(X)
print(y)

print(X.shape)
print(y.shape)

print(data.feature_names)
print(data.target_names)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.01,random_state=42)  # test_size = 0.2 -> accuracy lowers

model = GaussianNB()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print(y_pred)
print(y_test)

print(accuracy_score(y_test,y_pred))
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

sample = X_test[0].reshape(1,-1)   # Get the first sample from the test dataset.  (30,) to (1,30)
pred = model.predict(sample)
print("Predicted class is : ",data.target_names[pred])
s2 = X_test[5].reshape(1,-1)
pred2 = model.predict(s2)
print("Predicted class is : ",data.target_names[pred2])
s3 = X_test[0].reshape(1,-1)
pred3 = model.predict(s3)
print("Predicted class is : ",data.target_names[pred3])

"""
Reshaping is needed because Scikit-learn expects the input to model.predict() in a specific format.

Think of it this way

Your model was trained with data like this:

X_train
↓
[ [feature1, feature2, feature3, ...],
  [feature1, feature2, feature3, ...],
  [feature1, feature2, feature3, ...] ]

This is a 2D array:

(number of samples, number of features)

For the breast cancer dataset:

(563, 30)

That means:

563 samples
30 features per sample
But when you select one sample

You write:

X_test[0]

You get:

[17.99, 10.38, 122.8, ...]

Its shape is:

(30,)

This is a 1D array.

But model.predict() expects a 2D array, even if you're predicting only one sample.

It expects:

(number of samples, number of features)

So for one sample with 30 features, it expects:

(1, 30)
That's why we use
X_test[0].reshape(1, -1)

It changes:

(30,)

into:

(1, 30)

"""
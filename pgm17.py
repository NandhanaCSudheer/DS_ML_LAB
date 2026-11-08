from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay
import matplotlib.pyplot as plt

data = load_iris()
X = data.data
y = data.target

model = tree.DecisionTreeClassifier()
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
tree.plot_tree(model) 

accuracy = accuracy_score(y_test,y_pred)
cm = confusion_matrix(y_test,y_pred)
print("Accuracy = ",accuracy_score(y_test,y_pred)*100)
print("Accuracy score: ",accuracy_score(y_test,y_pred))
print("Confusion matrix: ",confusion_matrix(y_test,y_pred))
print("Classification report: ",classification_report(y_test,y_pred))

display = ConfusionMatrixDisplay( confusion_matrix=cm, display_labels=data.target_names) 
display.plot(cmap="Blues") 
plt.title("Decision Tree - Confusion Matrix") 
plt.show() 

plt.bar(["Decision Tree"], [accuracy], color="green") 
plt.ylim(0, 1) 
plt.ylabel("Accuracy") 
plt.title("Decision Tree Accuracy") 
plt.show() 

tree.plot_tree(model,feature_names=data.feature_names,class_names=data.target_names,filled = True)
plt.show()

tree_rules = tree.export_text(model,feature_names=data.feature_names) 
print("\nDecision Tree Rules:") 
print(tree_rules) 
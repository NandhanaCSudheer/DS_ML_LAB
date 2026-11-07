from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text 
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay 
import matplotlib.pyplot as plt 

iris = load_iris() 
X = iris.data 
y = iris.target 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 
model = DecisionTreeClassifier(random_state=42) 
model.fit(X_train, y_train) 
y_pred = model.predict(X_test) 
accuracy = accuracy_score(y_test, y_pred) 
print("Accuracy:", accuracy * 100, "%") 
cm = confusion_matrix(y_test, y_pred) 
print("\nConfusion Matrix:") 
print(cm) 
display = ConfusionMatrixDisplay( confusion_matrix=cm, display_labels=iris.target_names ) 
display.plot(cmap="Blues") 
plt.title("Decision Tree - Confusion Matrix") 
plt.show() 
new_flower = [[5.1, 3.5, 1.4, 0.2]] 
prediction = model.predict(new_flower) 
print("\nPredicted class:", iris.target_names[prediction[0]]) 
plt.figure(figsize=(6, 4)) 
plt.bar(["Decision Tree"], [accuracy], color="green") 
plt.ylim(0, 1) 
plt.ylabel("Accuracy") 
plt.title("Decision Tree Accuracy") 
plt.show() 
plt.figure(figsize=(20, 10)) 
plot_tree( model, feature_names=iris.feature_names, class_names=iris.target_names, filled=True, rounded=True, fontsize=10 ) 
plt.title("Decision Tree - Iris Dataset") 
plt.show() 
tree_rules = export_text(model,feature_names=iris.feature_names) 
print("\nDecision Tree Rules:") 
print(tree_rules) 
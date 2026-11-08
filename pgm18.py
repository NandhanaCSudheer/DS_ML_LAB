from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("pgm18.csv")
X = data[["Student_ID","Attendance_Percentage","Study_Hours_Per_Week","Internal_Marks_Out_Of_50"]]
y = data["Final_Result"]

model = tree.DecisionTreeClassifier(random_state=42)
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

sample = pd.DataFrame({"Student_ID":[31],"Attendance_Percentage":[68],"Study_Hours_Per_Week":[12],"Internal_Marks_Out_Of_50":[34]})
pred = model.predict(sample)
print(pred[0])

display = ConfusionMatrixDisplay( confusion_matrix=cm, display_labels=["Pass","Fail"]) 
display.plot(cmap="Blues") 
plt.title("Decision Tree - Confusion Matrix") 
plt.show() 

plt.bar(["Decision Tree"], [accuracy], color="green") 
plt.ylim(0, 1) 
plt.ylabel("Accuracy") 
plt.title("Decision Tree Accuracy") 
plt.show() 

tree.plot_tree(model,feature_names=["Student_ID","Attendance_Percentage","Study_Hours_Per_Week","Internal_Marks_Out_Of_50"],
               class_names=["Pass","Fail"],filled = True)
plt.show()

tree_rules = tree.export_text(model,feature_names=X.columns) 
print("\nDecision Tree Rules:") 
print(tree_rules) 
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
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

sample = pd.DataFrame({"Student_ID":[31],"Attendance_Percentage":[68],"Study_Hours_Per_Week":[12],"Internal_Marks_Out_Of_50":[34]})
pred = model.predict(sample)
print(pred[0])

tree.plot_tree(model,feature_names=X.columns,class_names=["Pass","Fail"],filled = True)
plt.show()
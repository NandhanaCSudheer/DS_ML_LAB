from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("pgm14.csv")
X = data[["Annual_Income","Spending_Score"]]

model = KMeans(n_clusters=3,random_state=42,n_init=10)
model.fit(X)

labels = model.labels_
centers = model.cluster_centers_

print("Silhouette Score: ",silhouette_score(X,labels))

plt.scatter(X.iloc[:,0],X.iloc[:,1],c = labels, cmap = "viridis", label = "Clusters")
plt.scatter(centers[:,0],centers[:,1],color = "red", marker = "*", label = "Centroids")
plt.legend()
plt.show()
from sklearn import datasets 
from sklearn.cluster import KMeans 
import matplotlib.pyplot as plt 

iris =datasets.load_iris() 
X=iris.data[:,:2] 
km=KMeans(n_clusters=3,random_state=42,n_init=10) 
km.fit(X) 
print(km.labels_) 
print(km.cluster_centers_) 
labels=km.labels_ 
centers=km.cluster_centers_ 
plt.scatter(X[:,0],X[:,1],c=labels,cmap='viridis') 
plt.scatter(centers[:,0],centers[:,1],marker='X',s=200,label="Centroids") 
plt.xlabel("Sepal Length") 
plt.ylabel("Sepal Width") 
plt.title("K-Means Clustering") 
plt.legend() 
plt.show() 
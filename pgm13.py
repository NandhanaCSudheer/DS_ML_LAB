from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

data = load_iris()
X = data.data[:,[0,1]]

model = KMeans(n_clusters=3,random_state=42,n_init=10)
model.fit(X)
labels = model.labels_
centers = model.cluster_centers_

score = silhouette_score(X, labels)
print("\nSilhouette Score:", score)

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis", label="Clusters")
plt.scatter(centers[:, 0], centers[:, 1],color="red", marker="X", s=200, label="Centroids")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("K-Means Clustering on Iris Dataset")
plt.legend()
plt.show()
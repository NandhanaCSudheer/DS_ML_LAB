
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("new.csv")

X = data[["study_hours", "attendance"]]
y = data["result"]

k = KMeans(n_clusters=3, random_state=42, n_init=10)
k.fit(X)

labels = k.labels_

plt.figure(figsize=(12, 5))

# Actual results
plt.subplot(1, 2, 1)
plt.scatter(
    X["study_hours"], X["attendance"],
    c=y, cmap="prism", edgecolor="k"
)
plt.title("Actual Results")
plt.xlabel("Study Hours")
plt.ylabel("Attendance")

# K-Means clusters
plt.subplot(1, 2, 2)
plt.scatter(
    X["study_hours"], X["attendance"],
    c=labels, cmap="jet", edgecolor="k"
)
plt.scatter(
    k.cluster_centers_[:, 0],
    k.cluster_centers_[:, 1],
    marker="X", s=200, color="black", label="Centroids"
)
plt.title("Predicted Clusters")
plt.xlabel("Study Hours")
plt.ylabel("Attendance")
plt.legend()

plt.tight_layout()
plt.show()

print("Cluster labels:", labels)

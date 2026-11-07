# implement K means clustering using scikit-learn

import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs   #  make_blobs() is used to generate artificial/sample data for clustering.
import matplotlib.pyplot as plt

data,_ = make_blobs(n_samples=300)   # make_blobs() creates artificial data points.. Create 300 data points.
# make_blobs() creates 2-dimensional data by default. make_blobs() actually returns two things: data & labels but we need only data (that why _)
data      # This simply displays the generated array when running in a Jupyter Notebook or similar environment.

kmeans = KMeans(n_clusters=5, random_state=42, n_init="auto").fit(data)  
# KMeans()  ->  Creates a K-Means clustering model. n_clusters ->   Divide the data into 5 clusters.
# n_init = "auto" -> controls how many times K-Means tries different initial centroid positions before choosing a result. "auto" lets Scikit-learn determine the appropriate behavior.


labels = kmeans.labels_     #   K-Means assigns every data point to a cluster.
set(labels)    #  set() removes duplicate values.

centroids = kmeans.cluster_centers_    #  gives the center point of each cluster.( here 5 centroids)

plt.scatter(data[:,0],data[:,1],c = labels,cmap = 'viridis')  # This creates the scatter plot.
# data[:,0] -> Take all rows from column 0. This gives the X coordinates. data[:,1] -> Take all rows from column 1.This gives the Y coordinates.
# c = labels ->  Color each point according to its cluster label. cmap = 'viridis' -> Specifies the color map used for the clusters.

plt.scatter(centroids[:,0],centroids[:,1],color = "red",marker = "x") # This plots the 5 centroids.marker = "x" -> makes each centroid appear as an X.

plt.legend(list(labels))  #  This attempts to create a legend using the cluster labels.

plt.scatter([2,6],[-4,6],color = "red")   # This plots two new points
plt.show()

kmeans.predict([[2,-4],[6,6],[6,-2]])    #  K-Means finds the nearest cluster centroid for each point and returns the cluster number.
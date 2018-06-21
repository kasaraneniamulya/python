import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from numpy import genfromtxt


X = pd.read_csv(r'C:\Users\Amuly\Desktop\Python_Lesson6\Python_Lesson6\sample_stocks.csv',dtype={"dividend": float, "returns": int})#loading sample_stocks file
X= np.array(X)
print(X)

kmeans = KMeans(n_clusters=4) #taking clusters as 4
kmeans.fit(X) #fitting our model to the training data

centroids = kmeans.cluster_centers_ #we are taking cluster centers as centroids
labels = kmeans.labels_  # eg :minus values as 1 , 0 values as 0
print(kmeans.labels_)

colors = ["g.","r.","c.","y."] #assigning colors to the clusters

for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10) # plotting data corresponding to the row nd column
plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, zorder=10)  #using x symbol for centroid

plt.show()

#extra
Nc = range(1, 20)

kmeans = [KMeans(n_clusters=i) for i in Nc]

kmeans

score = [kmeans[i].fit(X).score(X) for i in range(len(kmeans))]

score

plt.plot(Nc,score)

plt.xlabel('Number of Clusters')

plt.ylabel('Score')

plt.title('Elbow Curve')

plt.show()
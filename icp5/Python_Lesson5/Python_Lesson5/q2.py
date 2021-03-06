import numpy as np
import matplotlib.pyplot as plt
import random

def create_cluster(X, centroid_pts):
    cluster = {}
  # read about lambdas and np.linalg.form
  # https://stackoverflow.com/questions/32141856/is-norm-equivalent-to-euclidean-distance ,
  # here we are using order 1 to calculate normalized distance
    for x in X:
        value = min([(i[0],np.linalg.norm(x - centroid_pts[i[0]]))for i in enumerate(centroid_pts)], key=lambda s:s[1])[0]
        try:
            cluster[value].append(x)
        except:
            cluster[value] = [x]
    return cluster


def calculate_new_center(cluster):
    keys =sorted(cluster.keys())
    newmu = np.array([(np.mean(cluster[k],axis = 0))for k in keys])
    return newmu

def matched(new_centroids, old_centroids):
    return (set([tuple(a)for a in new_centroids]) == set([tuple(a)for a in old_centroids]))

def Apply_Kmeans(X, K, N):
    # selecting random centroids from dataset and by number of clusters.
    old_centroids = np.random.randint(N, size = K) # learray length of height=17 & k=3 now it creates random array of length 3 of values between 3 and 17
    old_centroid_pts = np.array([X[i]for i in old_centroids]) #if old centroid array =[3,8,1] the arrays in positions of 1,3,8 in X are considered as old centroid points

    print("old :",old_centroids)
    print(old_centroid_pts)

    cluster_info = create_cluster(X, old_centroid_pts) #A cluster is created with array X and old centroid points

    print("Initial cluster information:")
    print(cluster_info)

    new_centroid_pts=calculate_new_center(cluster_info) #mean of the cluster is calculated and new centroid points are formed
    print("new :", new_centroid_pts)
    itr = 0
    print("Graph after selecting initial clusters with initial centroids:")
    plot_cluster(old_centroid_pts,cluster_info,itr)
    while not matched(new_centroid_pts, old_centroid_pts): #if new and old centroids are not matched iteration continues
        itr = itr + 1
        old_centroid_pts = new_centroid_pts
        cluster_info = create_cluster(X,new_centroid_pts)
        plot_cluster(new_centroid_pts, cluster_info,itr)
        new_centroid_pts = calculate_new_center(cluster_info)

    print("Results after final iteration:")
    plot_cluster(new_centroid_pts, cluster_info, itr)
    return

def plot_cluster(mu,cluster, itr):
    color = 10 * ['r.','g.','k.','c.','b.','m.']
    print('Iteration number : ',itr)
    for l in cluster.keys():
        for m in range(len(cluster[l])):
            plt.plot(cluster[l][m][0], cluster[l][m][1], color[l], markersize=10) #color of first cluster is red
    plt.scatter(mu[:,0],mu[:,1],marker = 'x', s = 150, linewidths = 5, zorder = 10)
    plt.show()

def init_graph(N, p1, p2):
    X = np.array([(random.choice(p1),random.choice(p2))for i in range(N)])
    print(X)
    return X


def Simulate_Clusters():
    print(".........Starting Cluster Simulation.........")
    K = int(input('Enter the number of Clusters.......'))
    print('Now Enter the bounds for choosing uniform value....\n')
    Height= [33.23,34,35.4,31.6,33,36,35.1,34.3,28,29.3,40,30,32.5,33.3,29.5,35.1,34.7] #we assigned values for height and weight
    Weight= [18,20,22,24,26,28]
    N = len(Height) #array length of height  which is 17 in above case
    X = init_graph(N, Height, Weight )#now we are passing N,H,W values to the init_graph method
    plt.scatter(X[:, 0], X[:, 1], ) #corresponding height and weight are scattered
    plt.show()
    temp = Apply_Kmeans(X, K, N)#calling kmeans method


if __name__ == '__main__':
    Simulate_Clusters()  #simulate clusters method is called

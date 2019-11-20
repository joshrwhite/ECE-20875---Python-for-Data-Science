from cluster import *
from point import *

def kmeans(pointdata, clusterdata) :
    #Fill in
    
    #1. Make lists of points and clusters using makePointList and createClusters
    points = makePointList(pointdata)
    clusters = createClusters(clusterdata)
    #2. As long as points keep moving:
    while(1):
        #A. Move every point to its closest cluster (use Point.closest and
        #   Point.moveToCluster
        #   Hint: keep track here whether any point changed clusters by
        #         seeing if any moveToCluster call returns "True"
        retval = set()
        coord_list = list()
        cluster_list = list()
        for i in clusters:
            coord_list.append(i.coords)
            cluster_list.append(i)
        for i in points:
            #c = i.closest(coord_list)
            c = i.closest(cluster_list)
            #ind = coord_list.index(c)
            #r = i.moveToCluster(cluster_list[ind])
            r = i.moveToCluster(c)
            retval.add(r)

        #B. Update the centers of each cluster (use Cluster.updateCenter)    
        for i in clusters:
            i.updateCenter()

        if not True in retval:
            break
    #3. Return the list of clusters, with the centers in their final positions
    return clusters
    
    
    
if __name__ == '__main__' :
    data = np.array([[0.5, 2.5], [0.3, 4.5], [-0.5, 3], [0, 1.2], [10, -5], [11, -4.5], [8, -3]], dtype=float)
    centers = np.array([[0, 0], [1, 1]], dtype=float)
    
    clusters = kmeans(data, centers)
    for c in clusters :
        c.printAllPoints()
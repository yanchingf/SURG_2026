
import numpy as np
import scipy
import sklearn
from sklearn.cluster import AgglomerativeClustering

# aggregative hierarchical clustering
def cluster(data, n):
    clustering = AgglomerativeClustering(n)
    labels = clustering.fit_predict(data)
    agg = AgglomerativeClustering(distance_threshold=0, n_clusters=None, compute_distances=True)
    agg.fit(data)



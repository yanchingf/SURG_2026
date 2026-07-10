
import heapq
import math

import numpy as np
from astropy.coordinates import SkyCoord


class Node:

    def __init__(self, range=0, active=True, id=-1, cluster_id=-2, not_2d=False, coords=None):
        
        self.range = range
        self.id = id
        self.cluster_id = cluster_id
        self.active = active

        if len(coords) != 0:
            self.pos = coords
        else:
            print("ERROR: coords needed in declaration")

    def __repr__(self):

        return f"Range: {self.range} | ID: {self.id} | Cluster ID: {self.cluster_id} | Active: {self.active}"

        
class Graph:

    def __init__(self, n):

        self.nodes = {i: Node(id=i, cluster_id=i) for i in range(n)}
        self.adj = [[0]*n for i in range(n)] # full adj matrix
        self.group_ids = {i: [i] for i in range(n)} # each in own cluster originally

        self.length = n

    def add_edge(self, u, v, weight):

        self.adj[u][v] = weight
        self.adj[v][u] = weight

    def remove_edge(self, u, v):

        self.adj[u][v] = 0
        self.adj[v][u] = 0

    def get_edge(self, u, v):

        return self.adj[u][v]
    
    def set_node_status(self, id, status):

        self.nodes[id].active = status

    def get_cluster_members(self, cluster_id):

        return [i.id for i in self.nodes.values() if i.cluster_id==cluster_id]
    
    def merge_clusters(self, head, other):

        to_change = self.get_cluster_members(other)
        for i in to_change:
            self.nodes[i].cluster_id = self.nodes[head].cluster_id

    def djikstra(self, id):

        distances = [float("inf")] * self.length
        distances[id] = 0
        pq = [(0, id)]

        while len(pq) > 0:
            curr_dist, u = heapq.heappop(pq)

            if curr_dist > distances[u]:
                continue

            if not self.nodes[u].active:
                continue

            for v, weight in enumerate(self.adj[u]):
                if not self.nodes[v].active:
                    continue

                new_dist = curr_dist + weight

                if new_dist < distances[v]:
                    distances[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

        return distances

# update to be more general— extend to 3D points
def build_graph(points, ranges):

    points = np.asarray(points, dtype=float)
    ranges = np.asarray(ranges, dtype=float)
    n = points.shape[0]
    g = Graph(n)

    for i in range(n):
        g.nodes[i].pos = points[i]
        g.nodes[i].range = ranges[i]

    for i in range(n):
        for j in range(i + 1, n):
            d = np.linalg.norm(points[i] - points[j])
            if d <= ranges[i] and d <= ranges[j]:
                g.add_edge(i, j, 1/max(d, 1e-9))

    return g
 

import heapq
import math

class Node:

    def __init__(self, range=0, active=True, id=-1, cluster_id=-2, x=0, y=0):
        
        self.range = range
        self.id = id
        self.cluster_id = cluster_id
        self.active = active
        self.x = x
        self.y = y

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

            for v, weight in self.adj[u].enumerate():
                if not self.nodes[v].active:
                    continue

                new_dist = curr_dist + weight

                if new_dist < distances[v]:
                    distances[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

        return distances


def build_graph(x_arr, y_arr, ranges):

    n = len(x_arr)
    g = Graph(n)
    
    for i in range(n):
        g.nodes[i].x = x_arr[i]
        g.nodes[i].y = y_arr[i]
        g.nodes[i].range = ranges[i]

    for i in range(n):
        for j in range(i + 1, n):
            d = math.sqrt((x_arr[i] - x_arr[j])**2 + (y_arr[i] - y_arr[j])**2)
            g.add_edge(i, j, d)

    return g   

import heapq

class Node:

    def __init__(self, range=0, active=True, id=-1, cluster_id=-2, x=0, y=0):
        self.range = range
        self.id = id
        self.cluster_id = cluster_id
        self.active = active
        self.coords = (self.x, self.y)

    def __repr__(self):
        print(f"Range: {self.range} | ID: {self.id} | Cluster ID: {self.cluster_id} | Active: {self.active}")


class Graph:

    def __init__(self, n):

        self.nodes = {i: Node(id=i, cluster_id=i) for i in range(n)}
        self.adj = {i : {} for i in range(n)} # sparse adj
        self.group_ids = {i: [i] for i in range(n)} # each in own cluster originally

        self.length = n

    def add_edge(self, u, v, weight):
        self.adj[u][v] = weight
        self.adj[v][u] = weight

    def remove_edge(self, u, v):
        self.adj[u].pop(v, None)
        self.adj[v].pop(u, None)

    def get_edge(self, u, v):
        return self.adj[u][v]
    
    def set_node_status(self, id, status):
        self.nodes[id].active = False

    def get_cluster_members(self, cluster_id):
        return [i.id for i in self.nodes if i.cluster_id==cluster_id]
    
    def merge_clusters(self, head, other):
        to_change = self.get_cluster_members(other)
        for i in to_change:
            self.nodes[i].cluster_id = self.nodes[head].cluster_id

    def djikstra(self, node):
        distances = [0] * self.length
        distances[node.id] = 0
        return
    


class Node:

    def __init__(self, range=0, active=False, id=-1, cluster_id=-2):
        self.range = range
        self.id = id
        self.cluster_id = cluster_id
        self.active = active

    def __string__(self):
        print(f"Range: {self.range} | ID: {self.id} | Cluster ID: {self.cluster_id} | Active: {self.active}")


class Graph:

    def __init__(self, n):
        self.nodes = []*n
        self.length = n
    
    def djikstra(self, node):
        distances = [] * self.length
        distances[node.id] = 0
        return
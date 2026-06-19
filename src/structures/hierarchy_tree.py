
from graph import Graph
import heapq

class Hierarchy_Tree:

    def __init__(self, nodes):
        self.graph = heapq.heapify(nodes) # groupid by radius

    def add(self, node):
        heapq.heappush(self.nodes, node)
    
    def pop(self):
        return heapq.heappop(self.nodes)
    
    def push_pop(self, node):
        return heapq.heappushpop(self.nodes, node)
    
    def replace(self, node):
        return heapq.heapreplace(self.nodes, node)


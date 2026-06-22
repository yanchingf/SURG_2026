import heapq
import math
from graph import Graph

def in_range(graph, u, v):
    
    d = math.sqrt(graph.nodes[u].range**2 + graph.nodes[v].range**2)
    return d <= graph.nodes[u].range and d <= graph.nodes[v].range


def search(graph): # helper func for finding largest interaction

    curr = (-1, None, None)

    for i in graph.nodes.items():
        if i.range > curr[0] and i.active:
            curr = (i.range, i.id, "Node")
        
        # check all edges from node
        for v, weight in graph.adj[i.id].items():
            ok = in_range(graph, i.id, v)
            if weight > curr[0] and ok:
                curr = (weight, (i.id, v), "Edge")

    return curr # return type to decimate, exact interaction 

def decimate(graph, id):  # remove id, recalculate all edges

    # use heapq to find max interaction


    
    return
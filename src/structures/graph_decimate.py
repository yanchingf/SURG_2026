
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

def decimate(graph, obj):  # remove id, recalculate all edges

    if obj[2] == "Node":

        neighbors = [i.id for i in graph.adj[obj[1]].items()]

        graph.adj.remove(id)

        r = len(neighbors)

        for i in range(r):
            for j in range(i+1, r):

                u, v = neighbors[i][j]

                if in_range(graph, u, v):
                    graph.adjacent[u][v] = max(u.range, v.range) # check about this
                    graph.adjacent[v][u] = max(u.range, v.range)
                
        graph.set_node_status(obj[1], False) 
        for i in graph.adj[obj[1]].keys():
            graph.remove_edge(obj[1], i)
        
        graph.merge_clusters(neighbors[0], neighbors[1:]) # reassign group ids

    else:
        graph.remove_edge(obj[1][0], obj[1][1]) # renormalize

    return 
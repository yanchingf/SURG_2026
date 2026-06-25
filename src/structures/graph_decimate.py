
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

import heapq
import math
from src.structures.graph import Graph

def in_range(graph, u, v):

    d = math.sqrt(graph.nodes[u].range**2 + graph.nodes[v].range**2)
    return d <= graph.nodes[u].range and d <= graph.nodes[v].range


def search(graph): # helper func for finding largest interaction

    curr = (-1, None, None)

    for node_id, node in graph.nodes.items():
        if node.range > curr[0] and node.active:
            curr = (node.traverse_range, node.id, "Node")
        
        # check all edges from node
        for v in range(graph.length):
            if v != node_id:
                weight = graph.adj[node_id][v]
                if weight > 0 and in_range(graph, node_id, v):
                    if weight > curr[0]:
                        curr = (weight, (node_id, v), "Edge")

    return curr # return type to decimate, exact interaction 

def decimate(graph, obj):  # remove id, recalculate all edges

    if obj[2] == "Node":

        node_id = obj[1]
        node_range = obj[0]

        neighbors = [v for v in range(graph.length) if graph.adj[node_id][v] > 0 and graph.nodes[v].active]

        r = len(neighbors)

        for i in range(r):
            for j in range(i+1, r):

                if (i != node_id and j != node_id) and (graph.nodes[i].active and graph.nodes[j].active):
                    
                    ni, nj = neighbors[i], neighbors[j]
                    J_ij = graph.adj[node_id][ni]
                    J_ik = graph.adj[node_id][nj]

                    # largest term field => new couplings generated,
                    # each calculated with strength J_jk ~= J_ij*J_ik / h_i

                    new_strength = max(graph.adj[ni][nj], J_ij * J_ik / node_range)
                    graph.adj[ni][nj] = new_strength
                    graph.adj[nj][ni] = new_strength
                
        graph.set_node_status(node_id, False)

        if len(neighbors) >= 1:
            head = neighbors[0]
            for other in neighbors[1:]:
                graph.merge_clusters(head, graph.nodes[other].cluster_id)

    else:

        # if coupling, connected sites i and j go into same cluster

        coupling_strength = obj[0]
        u, v = obj[1][0], obj[1][1]

        new_traverse = u.traverse_range * v.traverse_range / graph.adj[u][v]

        u.group_id = v.group_id
        u.traverse_range = new_traverse

    return 
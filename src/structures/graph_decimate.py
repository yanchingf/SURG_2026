
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

import heapq
import math
import random
from src.structures.graph import Graph


def in_range(graph, u, v):

    d = math.sqrt((graph.nodes[u].x - graph.nodes[v].x)**2 + 
                  (graph.nodes[u].y - graph.nodes[v].y)**2)
    return d <= graph.nodes[u].range and d <= graph.nodes[v].range


def search(graph): # helper func for finding largest interaction

    '''
    pq = []

    curr = (-1, None, None)

    for node_id, node in graph.nodes.items():
        if node.range > curr[0] and node.active:
            curr = (node.range, node.id, "Node")
        
        # check all edges from node, do edge decimation iff two nodes in range of each other
        for v in range(graph.length):
            if v != node_id and graph.nodes[v].active:
                weight = graph.adj[node_id][v]
                if weight > 0 and in_range(graph, node_id, v):
                    if weight > curr[0]:
                        curr = (weight, (node_id, v), "Edge")
      
    return curr # return type to decimate, exact interaction '''

    active = [i for i, n in graph.nodes.items() if n.active]
    if not active:
        return (-1, None, None)

    start = random.choice(active)

    # find nearest active neighbor by distance
    best_dist = float('inf')
    best_neighbor = None
    for v in range(graph.length):
        if v != start and graph.nodes[v].active and graph.adj[start][v] > 0:
            d = graph.adj[start][v]
            if d < best_dist:
                best_dist = d
                best_neighbor = v

    if best_neighbor is None:
        return (graph.nodes[start].range, start, "Node")

    local_max = max(graph.nodes[start].range, best_dist)

    if local_max== graph.nodes[start].range:
        return (graph.nodes[start].range, start, "Node")
    else:
        return (best_dist, (start, best_neighbor), "Edge")


def decimate(graph, obj):  # decimate node / edge

    if obj[2] == "Node":

        node_id = obj[1]
        node_range = obj[0]

        neighbors = [v for v in range(graph.length) if (graph.adj[node_id][v] > 0 
                     and graph.nodes[v].active) and in_range(graph, node_id, v)]

        r = len(neighbors)

        for i in range(r): 
            for j in range(i+1, r):

                if (i != node_id and j != node_id) and (graph.nodes[i].active and graph.nodes[j].active):

                    print("CONDITION PASSED")
                    
                    ni, nj = neighbors[i], neighbors[j]
                    J_ij = graph.adj[node_id][ni]
                    J_ik = graph.adj[node_id][nj]

                    # largest term field => new couplings generated,
                    # each calculated with strength J_jk ~= J_ij*J_ik / h_i

                    new_strength = max(graph.adj[ni][nj], J_ij * J_ik / node_range)
                    graph.adj[ni][nj] = new_strength
                    graph.adj[nj][ni] = new_strength

                    print(f"Updated edges between {ni} and {nj}")
                
        graph.set_node_status(node_id, False)

        for v in neighbors:
            graph.remove_edge(node_id, v)


    else:

        # if coupling, connected sites i and j go into same cluster

        coupling_strength = obj[0]
        u, v = graph.nodes[obj[1][0]], graph.nodes[obj[1][1]]
        v_id = v.id

        new_traverse = u.range + v.range - graph.adj[u.id][v_id]

        print(f"  Edge decimate: u={u.id} (cluster={u.cluster_id}) v={v.id} (cluster={v.cluster_id})")
        print(f"  in_range check: {in_range(graph, u.id, v.id)}")
        print(f"  adj weight: {graph.adj[u.id][v.id]}")

        graph.merge_clusters(u.id, v.cluster_id)
        u.range = new_traverse

        for v in graph.nodes.values(): # update for rest in cluster
            if v.cluster_id == u.cluster_id and v.active:
                v.range = new_traverse

        graph.set_node_status(v_id, False)
        for k in range(graph.length):
            if graph.adj[v_id][k] > 0:
                graph.remove_edge(v_id, k)

    return 
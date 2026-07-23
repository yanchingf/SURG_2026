
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

import heapq
import math
import random
from src.structures.graph import Graph

import numpy as np


def in_range(graph, u, v):

    d = graph.adj[u][v]
    return d <= graph.nodes[u].range and d <= graph.nodes[v].range


def search(graph):

    active = [i for i, node in graph.nodes.items() if node.active]

    for i in active:

        can_reach = False

        for j in active:

            if i == j:
                continue

            d = graph.adj[i][j]

            if d <= graph.nodes[i].range and d > 0:
                can_reach = True

                if d <= graph.nodes[j].range:
                    return (i, j)

        # i cannot reach any other active site
        if can_reach == False:
            return (i, None)

    return (None, None)


def filter_bond(graph, i, j): # check if bond ij should be filtered -> set to -1 in adj matrix if so

    neighbors = [v for v in range(graph.length) if (graph.adj[i][v] > graph.adj[i][j] 
                and graph.nodes[v].active) and (graph.adj[j][v] > graph.adj[i][j])] # look for possible third node
    
    l =  len(neighbors) 
    if l <= 0:
        return
    else:
        graph.adj[i][j] = -1
        return


def smart_search(graph):
    return 

def decimate(graph, obj):  # decimate node / edge

    updated = []

    if obj[1] is None:

        node_id = obj[0]
        node_range = graph.nodes[node_id].range

        neighbors = [v for v in range(graph.length) if (graph.adj[node_id][v] > 0 
                     and graph.nodes[v].active) and in_range(graph, node_id, v)]

        r = len(neighbors)

        for i in range(r): 
            for j in range(i+1, r):
                    
                ni, nj = neighbors[i], neighbors[j]
                J_ij = graph.adj[node_id][ni]
                J_ik = graph.adj[node_id][nj]

                # largest term field => new couplings generated,
                # each calculated with strength J_jk ~= J_ij*J_ik / h_i

                new_strength = max(graph.adj[ni][nj], J_ij * J_ik / node_range)

                if graph.adj[ni][nj] != new_strength:
                    updated.append(ni)
                    updated.append(nj)

                graph.adj[ni][nj] = new_strength
                graph.adj[nj][ni] = new_strength
                
        graph.set_node_status(node_id, False)

        for v in neighbors:
            graph.remove_edge(node_id, v)

    else:

        # if coupling, connected sites i and j go into same cluster
        u, v = graph.nodes[obj[0]], graph.nodes[obj[1]]
        if v.range > u.range:
            u, v = v, u
        v_id = v.id

        updated.append(u.id)
        updated.append(v.id)

        if in_range(graph, u.id, v_id):
            new_traverse = max(0, u.range + v.range - graph.adj[u.id][v_id])
        else:
            new_traverse = u.range # negative safeguard

        for k in range(graph.length):

            if not (k == u.id or k == v_id):

                best = min(graph.adj[u.id][k], graph.adj[v_id][k])
                graph.adj[u.id][k] = best
                graph.adj[k][u.id] = best

        graph.merge_clusters(u.id, v.cluster_id)
        u.range = new_traverse

        for vv in graph.nodes.values(): # update for rest in cluster
            if vv.cluster_id == u.cluster_id and vv.active:
                vv.range = new_traverse
                updated.append(vv.id)

        graph.set_node_status(v_id, False)
        for k in range(graph.length):
            if graph.adj[v_id][k] > 0:
                graph.remove_edge(v_id, k)

    return


def repair(graph):

    n = len(graph.nodes)

    for i in range(n):
        for j in range(i + 1, n):

            if graph.nodes[i].active and graph.nodes[j].active and in_range(graph, i, j):

                if graph.adj[i][j] == 0:
                    d = np.linalg.norm(graph.nodes[i].pos - graph.nodes[j].pos)
                    graph.add_edge(i, j, d)

    return graph
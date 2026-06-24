
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
            curr = (i.traverse_range, i.id, "Node")
        
        # check all edges from node
        for v, weight in graph.adj[i.id].items():
            ok = in_range(graph, i.id, v)
            if weight > curr[0] and ok:
                curr = (weight, (i.id, v), "Edge")

    return curr # return type to decimate, exact interaction 

def decimate(graph, obj):  # remove id, recalculate all edges

    if obj[2] == "Node":

        node_id = obj[1]
        node_range = obj[0]

        neighbors = graph.adj[node_id]

        r = len(neighbors)

        for i in range(r):
            for j in range(i+1, r):

                if (i != node_id and j != node_id) and (graph.nodes[i].active and graph.nodes[j].active):

                    J_ij, J_ik = neighbors[i], neighbors[j] 

                    # largest term field => new couplings generated,
                    # each calculated with strength J_jk ~= J_ij*J_ik / h_i

                    new_strength = max(graph.adj[i][j], J_ij * J_ik / node_range)
                    graph.adj[i][j] = new_strength
                    graph.adj[j][i] = new_strength
                
        graph.set_node_status(obj[1], False) 
        
        graph.merge_clusters(neighbors[0], neighbors[1:]) # reassign group ids

    else:

        # if coupling, connected sites i and j go into same cluster

        coupling_strength = obj[0]
        u, v = obj[1][0], obj[1][1]

        new_traverse = u.traverse_range * v.traverse_range / graph.adj[u][v]

        u.group_id = v.group_id
        u.traverse_range = new_traverse

    return 

import random
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.patches as mpatches

from ..structures import graph

def generate_samples(n=1, neg_x_lim=0, x_lim=5000, neg_y_lim=0, y_lim=5000): # placeholder range samples
    
    l = []

    x = np.random.randint(neg_x_lim, x_lim, size=n)
    y = np.random.randint(neg_y_lim, y_lim, size=n)

    return (x, y)


def generate_random_graph(n=1, neg_x_lim=0, x_lim=5000, neg_y_lim=0, y_lim=5000):

    g = graph(n)
    l = [0] * len(graph.nodes)

    points = generate_samples(n, neg_x_lim, x_lim, neg_y_lim, y_lim)
    sizes = []

    for i in range(n):
        g.nodes[i].x = points[0][i]
        g.nodes[i].y = points[1][i]
        g.nodes[i].range = np.rng.uniform() 

        sizes.append(g.nodes[i].range)

    plt.scatter(points[0], points[1], color=l, marker='o')
    plt.title(f"Randomly Generated Samples (n={n})")
    plt.xlim(neg_x_lim, x_lim)
    plt.ylim(neg_y_lim, y_lim)
    plt.show()

    return g

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

import random
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.patches as mpatches
from datetime import datetime

from src.structures.graph import Graph


def generate_samples(n=1, dims=2): # placeholder range samples

    if lims is None:
        lims = [(0, 5000)] * dims

    points = np.stack([np.random.randint(low, high, size=n) for (low, high) in lims], axis=1,)

    return points

def generate_random_graph(n=1, dims=2, lims=None, m_min=0, m_max=32):

    g = Graph(n)

    points = generate_samples(n, dims=dims, lims=lims)
    sizes = []

    for i in range(n):

        g.nodes[i].pos = points[i].astype(float)
        g.nodes[i].range = max(1, np.random.randint(m_min, m_max))
        sizes.append(g.nodes[i].range)

    for i in range(n):
        for j in range(i+1, n):
            g.add_edge(i, j, np.norm())

    if dims == 2:
        plt.scatter(points[:, 0], points[:, 1], c=range(n), marker='o')
        plt.title(f"Randomly Generated Samples (n={n})")
        plt.xlim(lims[0][0], lims[0][1])
        plt.ylim(lims[1][0], lims[1][1])

    return (g, points)



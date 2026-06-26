
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
from src.structures.graph_decimate import search
from src.structures.graph_decimate import decimate


def generate_samples(n=1, neg_x_lim=0, x_lim=5000, neg_y_lim=0, y_lim=5000): # placeholder range samples

    x = np.random.randint(neg_x_lim, x_lim, size=n)
    y = np.random.randint(neg_y_lim, y_lim, size=n)

    return (x, y)


def generate_random_graph(n=1, neg_x_lim=0, x_lim=5000, neg_y_lim=0, y_lim=5000, m_min=-6, m_max=32):

    g = Graph(n)

    points = generate_samples(n, neg_x_lim, x_lim, neg_y_lim, y_lim)
    sizes = []

    for i in range(n):
        g.nodes[i].x = points[0][i]
        g.nodes[i].y = points[1][i]

        g.nodes[i].range = max(1, np.random.randint(m_min, m_max)) # visible brightness starts at +6... not sure about max brightness? 

        sizes.append(g.nodes[i].range)

    for i in range(n):
        for j in range(i+1, n):
            g.add_edge(i, j, math.sqrt((g.nodes[i].x - g.nodes[j].x)**2 + 
                  (g.nodes[i].y - g.nodes[j].y)**2))

    plt.scatter(points[0], points[1], c=range(n), s=sizes, marker='o')
    plt.title(f"Randomly Generated Samples (n={n})")
    plt.xlim(neg_x_lim, x_lim)
    plt.ylim(neg_y_lim, y_lim)
    plt.show()

    return (g, points)

def plot_graph(g, points, n, iteration, neg_x_lim=0, x_lim=5000, neg_y_lim=0, y_lim=5000,
               output_dir=os.path.join(os.path.dirname(__file__), '..', 'tests', 'random-plots')):
    
    os.makedirs(output_dir, exist_ok=True)

    x, y, colors, sizes = [], [], [], []

    ranges = [g.nodes[i].range for i in range(n)]

    for i in range(n):

        x.append(points[0][i])
        y.append(points[1][i])

        colors.append(g.nodes[i].cluster_id)

        # need scaling for neg min size?
        sizes.append(max(0.001, g.nodes[i].range))

    plt.figure()
    plt.scatter(x, y, c=colors, marker='o', s=ranges)
    plt.title(f"SDRG Step {iteration} | {len(x)} active nodes")
    plt.xlim(neg_x_lim, x_lim)
    plt.ylim(neg_y_lim, y_lim)
    plt.savefig(os.path.join(output_dir, f"step_{iteration}.png"))
    plt.close()


def run_sdrg_random(n=1, neg_x_lim=0, x_lim=5000, neg_y_lim=0, y_lim=5000):

    obj = generate_random_graph(n, neg_x_lim, x_lim, neg_y_lim, y_lim)
    g = obj[0]
    points = obj[1]

    iteration = 1
    
    curr = search(g)

    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'tests', 'random-plots', run_id)

    plot_graph(g, points, n, iteration=0, neg_x_lim=neg_x_lim, x_lim=x_lim, 
               neg_y_lim=neg_y_lim, y_lim=y_lim, output_dir=output_dir) # initial


    while curr[1] != None:

        print(f"Step {iteration} | Ω={curr}") # print log
        for i in range(n):
            if g.nodes[i].active:
                print(f"    id={g.nodes[i].id} h={g.nodes[i].range} cluster={g.nodes[i].cluster_id}")

        decimate(g, curr)
        plot_graph(g, points, n, iteration, output_dir=output_dir)

        iteration += 1
        curr = search(g)


    print(f"Done at iteration {iteration}, plots saved to '{output_dir}/'")
    return g


run_sdrg_random(n=5, neg_x_lim=0, x_lim=5000, neg_y_lim=0, y_lim=5000)



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


from graph import Graph
from graph import build_graph
from graph_decimate import decimate
from graph_decimate import search
from graph_decimate import in_range
from src.data.random_test import generate_random_graph


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

    for i in range(n):
        if g.nodes[i].active:
            for j in range(i+1, n):
                if not g.nodes[j].active:
                    continue
                if g.adj[i][j] > 0:
                    plt.plot([points[0][i], points[0][j]],
                            [points[1][i], points[1][j]],
                            color='gray', lw=0.8, alpha=0.5, zorder=1)
                
    plt.scatter(x, y, c=colors, marker='o', s=ranges)
    plt.title(f"SDRG Step {iteration} | {len(x)} active nodes")
    plt.xlim(neg_x_lim, x_lim)
    plt.ylim(neg_y_lim, y_lim)
    plt.savefig(os.path.join(output_dir, f"step_{iteration}.png"))
    plt.close()


def run_sdrg(n=1, neg_x_lim=0, x_lim=5000, neg_y_lim=0, y_lim=5000, random=True, inp=None):

    if random:
        obj = generate_random_graph(n, neg_x_lim, x_lim, neg_y_lim, y_lim)
        g = obj[0]
        points = obj[1]

    else:
        if inp == None:
            print("INPUT REQUIRED")
            return
        
        g = build_graph(inp[0], inp[1], inp[2])
        points = (inp[0], inp[1])
        n = len(inp[0])

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


x, y, r = [100,200,350,480,520,670,790,810,100], [100,200,3,4,520,670,790,810,100], [13,28,38,4,5,65,790,8,100]
run_sdrg(5, 0, 10000, 0, 10000, True, None)
run_sdrg(5, 0, 10000, 0, 10000, False, (x, y, r))
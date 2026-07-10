
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

from structures.graph import Graph
from structures.graph import build_graph
from structures.graph_decimate import decimate
from structures.graph_decimate import search
from structures.graph_decimate import repair
from src.data.random_test import generate_random_graph


def plot_graph(g, points, n, iteration, neg_x_lim=0, x_lim=5000, neg_y_lim=0, y_lim=5000,
               output_dir=os.path.join(os.path.dirname(__file__), '..', 'tests','test-plots')):
    
    os.makedirs(output_dir, exist_ok=True)

    x, y, colors, sizes = [], [], [], []

    fig, ax = plt.subplots()

    for i in range(n):

        x.append(points[0][i])
        y.append(points[1][i])

        colors.append(g.nodes[i].cluster_id)

        # need scaling for neg min size?
        sizes.append(max(0.001, g.nodes[i].range))

    for i in range(n):
        if g.nodes[i].active:
            for j in range(i+1, n):
                if g.nodes[j].active and g.adj[i][j] > 0:
                    plt.plot([points[0][i], points[0][j]],
                            [points[1][i], points[1][j]],
                            color='gray', lw=0.8, alpha=0.5, zorder=1)
                

    for i in range(n): # add radius and nodes
        xx, yy = points[0][i], points[1][i]
        rr = g.nodes[i].range
        color = cm.tab10(g.nodes[i].cluster_id % 10 if g.nodes[i].active else "gray")

        ax.add_patch(mpatches.Circle((xx, yy), radius=rr, fill=True,
                                    facecolor=color, alpha=0.08, zorder=0))
        ax.annotate(f"id={i}", (xx, yy), textcoords="offset points",
                xytext=(5, 5), fontsize=7, color='black')
        ax.annotate(f"cluster_id={g.nodes[i].cluster_id}", (xx, yy), textcoords="offset points",
                xytext=(5, 15), fontsize=5, color='black')
        ax.scatter(xx, yy, c=[color], s=40, zorder=3)


    ax.set_title(f"SDRG Step {iteration} | {n} nodes")
    ax.set_xlim(neg_x_lim, x_lim)
    ax.set_ylim(neg_y_lim, y_lim)
    ax.set_aspect('equal')
    fig.savefig(os.path.join(output_dir, f"step_{iteration}.png"))
    plt.close(fig)


def run_sdrg(n=1, neg_x_lim=0, x_lim=5000, neg_y_lim=0, y_lim=5000, random=True, inp=None):

    if random:
        obj = generate_random_graph(n, neg_x_lim, x_lim, neg_y_lim, y_lim)
        g = obj[0]
        points = obj[1]

    else:
        if inp == None:
            print("INPUT REQUIRED")
            return
        
        g = build_graph((inp[0], inp[1]), inp[2])
        points = (inp[0], inp[1])
        n = len(inp[0])

    iteration = 1
    
    curr = search(g)

    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'tests', 'test-plots', run_id)

    plot_graph(g, points, n, iteration=0, neg_x_lim=neg_x_lim, x_lim=x_lim, 
               neg_y_lim=neg_y_lim, y_lim=y_lim, output_dir=output_dir) # initial


    while curr[1] != None:

        print(f"Step {iteration} | Ω={curr}") # print log
        for i in range(n):
            print(f"    id={g.nodes[i].id} h={g.nodes[i].range} cluster={g.nodes[i].cluster_id} active={g.nodes[i].active}")

        decimate(g, curr)
        plot_graph(g, points, n, iteration, neg_x_lim=neg_x_lim, x_lim=x_lim,
           neg_y_lim=neg_y_lim, y_lim=y_lim, output_dir=output_dir)

        iteration += 1

        curr = repair(g)
        curr = search(g)

    print(f"Done at iteration {iteration}, plots saved to '{output_dir}/'")
    return g


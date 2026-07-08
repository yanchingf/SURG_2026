
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
from graph_decimate import repair
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
        if g.nodes[i].active:
            xx, yy = points[0][i], points[1][i]
            rr = g.nodes[i].range
            color = cm.tab10(g.nodes[i].cluster_id % 10)

            ax.add_patch(mpatches.Circle((xx, yy), radius=rr, fill=True,
                                      facecolor=color, alpha=0.08, zorder=0))
            ax.annotate(f"id={i}", (xx, yy), textcoords="offset points",
                    xytext=(5, 5), fontsize=7, color='black')
            ax.annotate(f"cluster_id={g.nodes[i].cluster_id}", (xx, yy), textcoords="offset points",
                    xytext=(5, 15), fontsize=5, color='black')
            ax.scatter(xx, yy, c=[color], s=40, zorder=3)

        else:
            xx, yy = points[0][i], points[1][i]
            rr = g.nodes[i].range
            ax.add_patch(mpatches.Circle((xx, yy), radius=rr, fill=True,
                                      facecolor="grey", alpha=0.08, zorder=0))
            ax.annotate(f"id={i}", (xx, yy), textcoords="offset points",
                    xytext=(5, 5), fontsize=7, color='black')
            ax.annotate(f"cluster_id={g.nodes[i].cluster_id}", (xx, yy), textcoords="offset points",
                    xytext=(5, 15), fontsize=5, color='black')
            ax.scatter(xx, yy, c="grey", s=40, zorder=3)

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
        
        g = build_graph(inp[0], inp[1], inp[2])
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

'''
x = [200, 400]
y = [150, 150]
r = [10, 10]
'''

'''
x = [200, 400]
y = [150, 150]
r = [250, 250]
'''
'''
x = [100, 300]
y = [200, 200]
r = [200, 200]
'''

'''
x = [100, 200, 300, 100, 200, 300, 100, 200, 300]
y = [100, 200, 300, 200, 100, 200, 300, 300, 100]
r = [150, 300, 10, 150, 150, 10, 10, 10, 10]
'''

'''
x = [100, 200, 300, 100, 200, 300, 100, 200, 300]
y = [100, 200, 300, 200, 100, 200, 300, 300, 100]
r = [150, 400, 150, 10, 10, 10, 150, 10, 150]
'''

'''
x = [100, 150, 240, 290]
y = [200, 200, 200, 200]
r = [100, 60, 100, 60]
'''

'''
x = [100, 150, 240, 290]
y = [200, 200, 200, 200]
r = [60, 60, 100, 60]
'''

'''
x = [100, 200, 300, 300]
y = [100, 100, 100, 300]
r = [120, 120, 120, 250]
'''

x = [200, 400, 200, 400]
y = [200, 200, 400, 400]
r = [250, 250, 250, 250]

'''
x = [100, 200, 500]
y = [100, 100, 100]
r = [110, 110, 110]
'''

'''
x = [100, 200, 150]
y = [100, 100, 186.6]
r = [110, 110, 110]
'''

'''
x = [99, 100, 200]
y = [300, 300, 300]
r = [99, 99, 199]
'''

'''
x = [200, 300, 400]
y = [200, 200, 200]
r = [300, 300, 300]
'''

'''
x = [100, 400, 700]
y = [200, 200, 200]
r = [350, 350, 350]
'''

'''
x = [300, 100, 300, 500, 300]
y = [300, 300, 100, 300, 500]
r = [210, 210, 210, 210, 210]
'''




run_sdrg(5, 0, 750, 0, 750, False, (x, y, r))
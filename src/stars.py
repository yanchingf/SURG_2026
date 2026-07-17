
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.patches as mpatches

from data_handling.star_io import parse_star_data
from data_handling.star_io import save_processed_data
from data_handling.star_io import get_coords_and_brightness

from structures.graph import Graph
from structures.graph import build_graph
from structures.graph_decimate import decimate
from structures.graph_decimate import search
from structures.graph_decimate import repair
from src.data_handling.random_test import generate_random_graph

from astropy import units as u
from astropy.coordinates import Angle

'''
df = parse_star_data()
save_processed_data(df)
'''

def star_to_graph_mapping(skycoords): # need to update per iteration

    t = get_coords_and_brightness(skycoords)
    starcoords, brightness = t[0], t[1]

    n = skycoords.shape[0]
    coords = [[0,0] for i in range(n)]

    for i in range(n):
        ra = starcoords[i].ra
        dec = starcoords[i].dec
        coords[i][0], coords[i][1] = ra, dec

    return build_graph(coords, brightness)


def get_k_neighbors(coord, table): # get k closest stars from catalogue to the coord, check
    return 


def plot_star_map(starcoords, graph, iteration, output_dir):

    n = len(starcoords)

    ra = Angle(starcoords.ra).wrap_at(180 * u.deg)
    dec = Angle(starcoords.dec)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="mollweide")
    ax.scatter(ra.radian, dec.radian)
    ax.grid(True)

    for i in range(n-1):
        if graph.nodes[i].active == True:
            for j in range(i+1, n):
                if graph.nodes[j].active and graph.adj[i][j] > 0:
                    plt.plot([ra[i].radian, ra[j].radian],[dec[i].radian, dec[j].radian],
                            color='gray', lw=0.8, alpha=0.5, zorder=1)
                    
    for i in range(n):

        color = cm.tab10(graph.nodes[i].cluster_id % 10) if graph.nodes[i].active else "gray"

        ax.scatter(ra[i].radian, dec[i].radian, c=[color], s=40, zorder=3,)
        ax.annotate(f"id={i}", (ra[i].radian, dec[i].radian), xytext=(5, 5),
            textcoords="offset points", fontsize=7,)
        ax.annotate(f"cluster={graph.nodes[i].cluster_id}", (ra[i].radian, dec[i].radian),
            xytext=(5, 15), textcoords="offset points", fontsize=5,)


    ax.set_xticklabels([
        "14h", "16h", "18h", "20h", "22h",
        "0h", "2h", "4h", "6h", "8h", "10h"])

    ax.grid(True)

    fig.savefig(os.path.join(output_dir, f"step_{iteration}.png"))
    plt.close(fig)
                    
    





    
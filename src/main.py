
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

from data_handling.star_io import get_all_star_data, get_patch, get_coords_and_brightness
from structures.graph import build_graph
from structures.graph_decimate import decimate

from sdrg import run_sdrg


data = get_all_star_data()

c_lower_lim = 1
c_upper_lim = 5
c_range = list(range(c_lower_lim, c_upper_lim + 1))

patch_names = ["Cnc", "Ori", "UMa", "Cas", "Leo"]

output_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'output')
os.makedirs(output_dir, exist_ok=True)

for patch_name in patch_names:

    patch_df = get_patch(data, patch_name)

    if patch_df.shape[0] < 2:
        print(f"{patch_name}: not enough stars")
        continue

    num_clusters_by_c = []
    max_cluster_size_by_c = []
    size_dist_by_c = {}

    for c in c_range:

        coords, brightness = get_coords_and_brightness(patch_df, c=c)
        x, y = coords[0], coords[1]

        g = run_sdrg(
            n=len(x),
            neg_x_lim=0, x_lim=float(x.max()) + 1,
            neg_y_lim=0, y_lim=float(y.max()) + 1,
            use_random=False,
            inp=(x, y, brightness),
            percolation_stats=True,)

        cluster_sizes = Counter()
        for node in g.nodes:
            if node.active:
                cluster_sizes[node.cluster_id] += 1

    print(f"Done: {patch_name} ({len(c_range)} SDRG runs)")

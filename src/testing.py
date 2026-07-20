
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

from data_handling.star_io import get_all_star_data, get_patch, get_coords_and_brightness
from structures.graph import build_graph
from structures.graph_decimate import decimate

from datetime import datetime

from sdrg import run_sdrg
from astropy.coordinates import get_constellation
from stars import plot_star_map

data = get_all_star_data()

coords, brightness, skycoords = get_coords_and_brightness(data)

names = get_constellation(skycoords, short_name=True)
print(set(names))
print(pd.Series(names).value_counts().head(20))

print(len(data))
print(data.duplicated(subset=["HR"]).sum())
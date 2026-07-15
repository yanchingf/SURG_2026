
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from data.star_io import get_all_star_data


data = get_all_star_data()
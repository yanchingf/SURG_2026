
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import pandas as pd

class Sky:
    def __init__(self, pos_x, pos_y, magnitudes=None, spectral_types=None):
        self.positions_x = np.array(pos_x)
        self.positions_y = np.array(pos_y)
        self.magnitudes = np.array(magnitudes) if magnitudes is not None else None
        self.spectral_types = spectral_types  # list of strings

    def show(self):
        plt.plot(self.positions_x, self.positions_y, "o")
        plt.show()

    def show_custom(self):
        fig, ax = plt.subplots(figsize=(14, 7), facecolor='black')
        ax.set_facecolor('black')

        # Star size: brighter (lower magnitude) = bigger dot
        if self.magnitudes is not None:
            sizes = np.clip(30 - self.magnitudes * 4, 1, 60)
        else:
            sizes = 10

        # Star color by spectral type (OBAFGKM sequence)
        spectral_colors = {
            'O': '#9bb0ff', 'B': '#aabfff', 'A': '#cad7ff',
            'F': '#f8f7ff', 'G': '#fff4ea', 'K': '#ffd2a1', 'M': '#ffcc6f',
        }
        if self.spectral_types is not None:
            colors = [spectral_colors.get(s[0].upper(), 'white')
                      if s else 'white' for s in self.spectral_types]
        else:
            colors = 'white'

        ax.scatter(self.positions_x, self.positions_y,
                   s=sizes, c=colors, alpha=0.85, linewidths=0)

        ax.set_xlim(self.positions_x.min() - 5, self.positions_x.max() + 5)
        ax.set_ylim(self.positions_y.min() - 5, self.positions_y.max() + 5)
        ax.set_xlabel('Right Ascension (degrees)', color='grey')
        ax.set_ylabel('Declination (degrees)', color='grey')
        ax.set_title('Star Map', color='white', fontsize=14)
        ax.tick_params(colors='grey')
        for spine in ax.spines.values():
            spine.set_edgecolor('#333333')

        plt.tight_layout()
        plt.show()


def parse_ra(ra_str):
    """Convert hhmmss.s string to degrees."""
    ra_str = str(ra_str).strip()
    if len(ra_str) < 7:
        return None
    try:
        h = float(ra_str[0:2])
        m = float(ra_str[2:4])
        s = float(ra_str[4:])
        return (h + m / 60 + s / 3600) * 15  # hours -> degrees
    except ValueError:
        return None

def parse_dec(dec_str):
    dec_str = str(dec_str).strip()
    if len(dec_str) < 6:
        return None
    try:
        sign = -1 if dec_str[0] == '-' else 1
        d = float(dec_str[1:3])
        m = float(dec_str[3:5])
        s = float(dec_str[5:])
        return sign * (d + m / 60 + s / 3600)
    except ValueError:
        return None


def main():
    df = pd.read_csv('catalog.csv', dtype=str)

    ra_deg  = df['RA2000'].apply(parse_ra)
    dec_deg = df['Dec2000'].apply(parse_dec)
    vmag = pd.to_numeric(df['Vmag'], errors='coerce')
    stype = df['SpType'].fillna('').tolist()

    # Drop rows with missing coordinates
    mask = ra_deg.notna() & dec_deg.notna()
    sky = Sky(
        pos_x=ra_deg[mask].tolist(),
        pos_y=dec_deg[mask].tolist(),
        magnitudes=vmag[mask].tolist(),
        spectral_types=[stype[i] for i in ra_deg[mask].index],
    )

    sky.show_custom()


if __name__ == '__main__':
    main()
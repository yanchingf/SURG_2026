
import os
import numpy as np
import pandas as pd

from astropy.io import ascii
from astropy.table import Table
from astropy.coordinates import SkyCoord
import astropy.units as u
from astropy.coordinates import get_constellation

# via bright star catalogue docs
catalogue_fields = [ 
    (0, 4), # HR number
    (4, 14), # Name
    (14, 25), # DM identification
    (25, 31), # HD number
    (31, 37), # SAO number
    (75, 77), # RAh 
    (77, 79), # RAm 
    (79, 83), # RAs 
    (83, 84), # DE sign
    (84, 86), # DEd 
    (86, 88), # DEm 
    (89, 90), # DEs 
    (102, 107), # Vmag
    (109, 114), # B-V
    (127, 147), # Spectral type
]

field_names = [
    "HR", "Name", "DM", "HD", "SAO",
    "RAh", "RAm", "RAs",
    "DE_sign", "DEd", "DEm", "DEs",
    "Vmag", "B-V", "SpType",
]


def parse_star_data():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    CATALOG_PATH = os.path.join(
        BASE_DIR, '..', '..', 'data', 'raw-data', 'yale-data', 'catalog.txt')
    CATALOG_PATH = os.path.normpath(CATALOG_PATH)

    df = pd.read_fwf(
        CATALOG_PATH,
        colspecs=catalogue_fields,
        names=field_names,
        dtype=str,
    )

    for col in ("Name", "DM", "HD", "SAO", "DE_sign", "SpType"):
        df[col] = df[col].str.strip()


    numeric_cols = ["RAh", "RAm", "RAs", "DEd", "DEm", "DEs", "Vmag", "B-V"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["RAh", "RAm", "RAs", "DEd", "DEm", "DEs", "Vmag"])
    df = df.reset_index(drop=True)

    return df


def see_table(df, n=20): # display as astropy table

    table = Table.from_pandas(df.head(n) if n else df)
    table.pprint(max_lines=-1, max_width=-1)
    return table


def get_coords_and_brightness(df, c=1): # convert RA / Dec => numeric cartesian coords & Vmag to brightness

    ra = (df["RAh"].to_numpy(dtype=float)
        + df["RAm"].to_numpy(dtype=float) / 60
        + df["RAs"].to_numpy(dtype=float) / 3600) * u.hourangle

    dec_sign = np.where(df["DE_sign"] == "-", -1.0, 1.0)

    dec = (dec_sign * (
            df["DEd"].to_numpy(dtype=float)
            + df["DEm"].to_numpy(dtype=float) / 60
            + df["DEs"].to_numpy(dtype=float) / 3600)) * u.deg

    sky_coords = SkyCoord(ra=ra, dec=dec, frame="icrs")
    ra_deg = sky_coords.ra.to_value(u.deg)
    dec_deg = sky_coords.dec.to_value(u.deg)
    coords = np.column_stack((ra_deg, dec_deg))

    brightness = ((7.0-df["Vmag"])*c).to_numpy(dtype=float)

    return (coords, brightness, sky_coords)


def save_processed_data(df, filename="stars.csv"):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    output_dir = os.path.normpath(
        os.path.join(BASE_DIR, "..", "..", "data", "processed_data")
    )
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, filename)
    df.to_csv(output_path, index=False)

    print(f"Saved processed data to log.")


def get_patch(df, constellation, short_name=True):

    ra = (df["RAh"].to_numpy(dtype=float)
        + df["RAm"].to_numpy(dtype=float) / 60
        + df["RAs"].to_numpy(dtype=float) / 3600) * u.hourangle

    dec_sign = np.where(df["DE_sign"] == "-", -1.0, 1.0)
    dec = (dec_sign * (
            df["DEd"].to_numpy(dtype=float)
            + df["DEm"].to_numpy(dtype=float) / 60
            + df["DEs"].to_numpy(dtype=float) / 3600)) * u.deg

    sky_coords = SkyCoord(ra=ra, dec=dec, frame="icrs")
    names = get_constellation(sky_coords, short_name=short_name)
    mask = np.array(names) == constellation
    return df[mask].reset_index(drop=True)


def get_all_star_data():

    df = parse_star_data()
    save_processed_data(df=df,)
    return df

get_all_star_data()

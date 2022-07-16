"""
    Cosmic Cliffs, Carina Nebula, JWST
"""
from __future__ import annotations

from napari_nasa_samples.utils import get_array

def make_sample_data():
    """Generates an image"""
    array = get_array("https://stsci-opo.org/STScI-01G7WCH0VH9RK7YBFAMM07S2TB.tif")
    return [(array, {'name':'Cosmic Cliffs, Carina Nebula, JWST'})]


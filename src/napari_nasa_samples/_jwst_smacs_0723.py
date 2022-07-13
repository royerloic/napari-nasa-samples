"""
    Deep Field SMACS 0723, JWST
"""
from __future__ import annotations

from napari_nasa_samples.utils import get_array

def make_sample_data():
    """Generates an image"""
    array = get_array("https://stsci-opo.org/STScI-01G7DDBNAV8SHNRTMT9AHGC5MF.tif")
    return [(array, {'name':'Deep Field SMACS 0723, JWST'})]

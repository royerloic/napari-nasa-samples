"""
    Southern Ring Nebula, JWST
"""
from __future__ import annotations

from napari_nasa_samples.utils import get_array

def make_sample_data():
    """Generates an image"""
    array = get_array("https://stsci-opo.org/STScI-01G79R4PQEKTHV094X9767ASV8.tif")
    return [(array, {'name': "Southern Ring Nebula, JWST"})]

"""
    Messier 101, Hubble
"""
from __future__ import annotations

from napari_nasa_samples.utils import get_array

def make_sample_data():
    """Generates an image"""
    array = get_array("https://stsci-opo.org/STScI-01EVT7MPFFJ45VTXMZ8GAXV57W.tif")
    return [(array, {'name': "Messier 101, Hubble"})]

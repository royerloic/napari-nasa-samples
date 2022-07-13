"""
    Pillars of Creation, Hubble
"""
from __future__ import annotations

from napari_nasa_samples.utils import get_array

def make_sample_data():
    """Generates an image"""
    array = get_array("https://stsci-opo.org/STScI-01G5PGPAG5TD3KN2VMZ5NVESTJ.tif")
    return [(array, {'name': "Large Magellanic Cloud, Hubble"})]

"""
    Stephan's Quintet, JWST
"""
from __future__ import annotations

from napari_nasa_samples.utils import get_array

def make_sample_data():
    """Generates an image"""
    array = get_array("https://stsci-opo.org/STScI-01G7DAXJYYTYXCFSB8VQRK5X2F.tif")
    return [(array, {'name': "Stephan's Quintet, JWST"})]

"""
    Blue Marble image.
"""
from __future__ import annotations

from napari_nasa_samples.utils import get_array

def make_sample_data():
    """Generates an image"""
    array_east = get_array("http://eoimages.gsfc.nasa.gov/images/imagerecords/57000/57752/land_shallow_topo_east.tif")
    array_west = get_array("http://eoimages.gsfc.nasa.gov/images/imagerecords/57000/57752/land_shallow_topo_west.tif")
    return [(array_east, {'name': "Blue Marble, East, NASA"}),
            (array_west, {'name': "Blue Marble, West, NASA"})]

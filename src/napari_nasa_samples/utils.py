from os import getenv, makedirs

import requests
from os.path import join, exists
from sys import platform

from PIL import Image


def get_array(url):
    file_path = get_file_path(url)

    if not exists(file_path):
        download(url)

    if file_path.endswith('tif'):
        from tifffile import tifffile
        array = tifffile.imread(file_path)
    else:
        import imageio
        Image.MAX_IMAGE_PIXELS = None
        array = imageio.imread(file_path)
    return array

def download(url, chunk_size=1024*1024):
    get_response = requests.get(url, stream=True)
    file_path = get_file_path(url)
    with open(file_path, 'wb') as f:
        for chunk in get_response.iter_content(chunk_size=chunk_size):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)

    return file_path

def get_file_path(url):
    file_name = url.split("/")[-1]
    file_path = join(get_cache_folder(), file_name)
    return file_path


def get_home_folder():
    from pathlib import Path

    home_folder = f"{Path.home()}"
    return home_folder


def get_cache_folder():
    cache_folder = None

    if platform == "linux" or platform == "linux2":
        cache_folder = join(get_home_folder(), '.cache')

    elif platform == "darwin":
        cache_folder = join(get_home_folder(), '/Library/Caches')

    elif platform == "win32":
        cache_folder = join(get_home_folder(), getenv('LOCALAPPDATA'))

    try:
        makedirs(cache_folder)
    except Exception:
        pass

    if exists(cache_folder):
        return cache_folder
    else:
        return None
"""
Define functions to download and load the dataset
"""
from pathlib import Path
import gzip
import requests
import numpy as np

root_dir = Path(__file__).resolve(strict=True).parent.parent.parent
data_dir = root_dir / 'data'


def fetch(url):
    """
    @description: download and decompress data in the MNIST dataset
    """
    file_path = data_dir / url.split('/')[-1]

    if not file_path.is_file():
        with requests.get(url) as response:
            with file_path.open('wb') as file:
                file.write(response.content)

    with gzip.open(file_path, 'rb') as file:
        array = np.frombuffer(file.read(), np.int8)

    return array


if __name__ == '__main__':
    data_dir.mkdir(exist_ok=True)
    fetch("http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz")
    fetch("http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz")
    fetch("http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz")
    fetch("http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz")

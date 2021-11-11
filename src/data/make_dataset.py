"""
Define functions to download and load the dataset
"""
from pathlib import Path
import requests

root_dir = Path(__file__).resolve(strict=True).parent.parent.parent
data_dir = root_dir / 'data'


def download(url):
    """
    @description: download data from the MNIST dataset
    """
    file_path = data_dir / url.split('/')[-1]

    if not file_path.is_file():
        with file_path.open('wb') as file, requests.get(url) as response:
            file.write(response.content)


if __name__ == '__main__':
    data_dir.mkdir(exist_ok=True)
    download("http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz")
    download("http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz")
    download("http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz")
    download("http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz")

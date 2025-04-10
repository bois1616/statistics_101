import numpy as np # type: ignore[import]
from scipy.spatial.distance import pdist, squareform # type: ignore[import]
from rich import print

def pairwise_distances(data: np.ndarray) -> np.ndarray:
    return np.sum((data[None, :] - data[:, None])**2, axis=2)


def pairwise_distances2(data: np.array) -> np.array:
    return squareform(pdist(data))


if __name__ == '__main__':
    print('[bold red on yellow]Nur für Import, nicht ausführbar!\n')

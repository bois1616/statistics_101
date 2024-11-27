import numpy as np
from scipy.spatial.distance import pdist, squareform

def pairwise_distances(data: np.ndarray) -> np.ndarray:
    return np.sum((data[None, :] - data[:, None])**2, axis=2)


def pairwise_distances2(data: np.array) -> np.array:
    return squareform(pdist(data))


if __name__ == '__main__':
    print('\033[2J\033[H\nNur für Import, nicht ausführbar!\n')
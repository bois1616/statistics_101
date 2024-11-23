import numpy as np
from scipy.spatial.distance import pdist, squareform

def pairwise_distances(data: np.array) -> np.array:
   return np.sum((data[None, :] - data[:, None])**2, 2)


def pairwise_distances2(data: np.array) -> np.array:
    return squareform(pdist(data))


if __name__ == '__main__':
    data = np.array([[1, 2], [3, 4], [5, 6]])
    print(np.sqrt(pairwise_distances(data)))
    print(pairwise_distances2(data))
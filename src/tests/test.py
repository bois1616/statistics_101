import unittest
import numpy as np
from tools.tsne_tools import pairwise_distances

class TestPairwiseDistances(unittest.TestCase):
    def test_pairwise_distances(self):
        data = np.array([
            [1, 2],
            [3, 4],
            [5, 6]
        ])
        #data = np.sqrt(data)
        expected_result = np.array([
            [0.0, 2.8284271247461903, 5.656854249492381],
            [2.8284271247461903, 0.0, 2.8284271247461903],
            [5.656854249492381, 2.8284271247461903, 0.0]
        ])
        result = pairwise_distances(data)
        np.testing.assert_allclose(result, expected_result, rtol=1e-5, atol=1e-8)

if __name__ == '__main__':
    unittest.main()
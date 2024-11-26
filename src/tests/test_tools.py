import unittest
import numpy as np
from tools.tsne_tools import pairwise_distances, pairwise_distances2

class TestPairwiseDistances(unittest.TestCase):
    def setUp(self):
        self.data = np.array([
            [1, 2],
            [3, 4],
            [5, 6]
        ])
        
        self.expected_result = np.array([
            [0.0, 2.8284271247461903, 5.656854249492381],
            [2.8284271247461903, 0.0, 2.8284271247461903],
            [5.656854249492381, 2.8284271247461903, 0.0]
        ])
        
    def test_pairwise_distances(self):
        result = np.sqrt(pairwise_distances(self.data))
        np.testing.assert_allclose(result, self.expected_result, rtol=1e-5, atol=1e-8)
        
    def test_pairwise_distances2(self):
        result = pairwise_distances2(self.data)
        np.testing.assert_allclose(result, self.expected_result, rtol=1e-5, atol=1e-8)

if __name__ == '__main__':
    unittest.main()
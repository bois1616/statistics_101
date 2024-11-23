import unittest
from statistics.tools.tsne_tools import pairwise_distances

class TestPairwiseDistances(unittest.TestCase):
    def test_pairwise_distances(self):
        data = [
            [1, 2],
            [3, 4],
            [5, 6]
        ]
        expected_result = [
            [0.0, 2.8284271247461903, 5.656854249492381],
            [2.8284271247461903, 0.0, 2.8284271247461903],
            [5.656854249492381, 2.8284271247461903, 0.0]
        ]
        result = pairwise_distances(data)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
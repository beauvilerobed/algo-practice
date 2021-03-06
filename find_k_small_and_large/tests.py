import unittest
import random
from find_k_smallest import k_smallest, k_smallest_naive
from find_k_largest import k_largest, k_largest_naive


class KSmallestAndLargest(unittest.TestCase):
    def test_small_k_smallest(self):
        test_cases = [
            ([1, 1, 1], 2, None),
            ([9, 8, 7, 6, 5, 4, 3, 2, 1], 3, 3),
            ([1, 1, 3, 4], 2, 3),
            ([], 100, None)
        ]
        for nums, k, answer in test_cases:
            self.assertEqual(k_smallest(nums, k), answer)

    def test_small_k_largest(self):
        test_cases = [
            ([1, 1, 1], 2, None),
            ([9, 8, 7, 6, 5, 4, 3, 2, 1], 3, 7),
            ([1, 1, 3, 4], 2, 3),
            ([], 100, None)
        ]
        for nums, k, answer in test_cases:
            self.assertEqual(k_largest(nums, k), answer)

    def test_large_k_smallest(self):
        test_cases = [
            ([1] * 10 ** 5, 2, None),
            ([i for i in range(10 ** 5 + 1)], 10 ** 5, 10 ** 5 - 1),
            ([(i + 1) % 10 for i in range(10 ** 5)], 5, 4)
        ]
        for nums, k, answer in test_cases:
            self.assertEqual(k_smallest(nums, k), answer)

    def test_large_k_largest(self):
        test_cases = [
            ([1] * 10 ** 5, 2, None),
            ([i for i in range(10 ** 5 + 1)], 10 ** 5, 1),
            ([(i + 1) % 10 for i in range(10 ** 5)], 5, 5)
        ]
        for nums, k, answer in test_cases:
            self.assertEqual(k_largest(nums, k), answer)

    def test_stress_k_smallest(self):
        test_cases = [([random.randint(1, 1000)
                      for _ in range(random.randint(50, 100))],
                      random.randint(50, 100))
                      for _ in range(1000)]
        for nums, k in test_cases:
            self.assertEqual(k_smallest(nums, k), k_smallest_naive(nums, k))

    def test_stress_k_largest(self):
        test_cases = [([random.randint(1, 1000)
                      for _ in range(random.randint(50, 100))],
                      random.randint(50, 100))
                      for _ in range(1000)]
        for nums, k in test_cases:
            self.assertEqual(k_largest(nums, k), k_largest_naive(nums, k))


if __name__ == '__main__':
    unittest.main()

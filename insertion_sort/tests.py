import unittest
import random
from insertion_sort import insertion_sort


class InsertionSort(unittest.TestCase):
    def test_small(self):
        test_case = [
            ([2, 1, 1], [1, 1, 2]),
            ([2, 3, 0], [0, 2, 3]),
            ([], []),
            ([4, 3, 2, 1, 9, 7, 6, 0], [0, 1, 2, 3, 4, 6, 7, 9]),
        ]
        for nums, answer in test_case:
            self.assertEqual(insertion_sort(nums), answer)

    def test_large(self):
        test_case = [
            ([10 ** 3 - 1 - k for k in range(10 ** 3)], [k for k in range(10 ** 3)]),
        ]
        for nums, answer in test_case:
            self.assertEqual(insertion_sort(nums), answer)

    def test_stress(self):
        test_cases = [[random.randint(1, 1000) for _ in range(random.randint(50, 100))] for _ in range(random.randint(50, 100))]
        for nums in test_cases:
            answer = sorted(nums)
            if insertion_sort(nums) != answer:
                print(nums)
            self.assertEqual(insertion_sort(nums), answer)


if __name__ == '__main__':
    unittest.main()
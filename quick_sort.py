""" QuickSort algorithm illustrated in python.
"""

import unittest


def quick_sort(x: list) -> list:
    """ Sort a list of numbers.

    Example:
      >>> quick_sort([3, 2, 1, 0, 4, 5])
      [0, 1, 2, 3, 4, 5]
    """

    # Choose pivot and move it to index 0 here

    array_2_start_i = len(x)

    if len(x) == 2:
        if x[0] > x[1]:
            return [x[1], x[0]]
        else:
            return x

    if len(x) < 2:
        return x

    i = 1
    end_i = len(x)
    while True:
        if x[i] > x[0]:
            x.append(x.pop(i))
            i -= 1
            end_i -= 1
            array_2_start_i -= 1
        i += 1
        if i >= end_i:
            break

    if array_2_start_i > 1:
        smaller_than_pivot = x[1:array_2_start_i]
    else:
        smaller_than_pivot = []

    if array_2_start_i < len(x):
        bigger_than_pivot = x[array_2_start_i:]
    else:
        bigger_than_pivot = []

    return quick_sort(smaller_than_pivot) + [x[0]] + quick_sort(bigger_than_pivot)


class TestQuickSort(unittest.TestCase):
    def setUp(self):
        pass

    def test_n_is_2(self):
        self.assertListEqual(
            quick_sort([7, 2]),
            [2, 7])

    def test_n_is_2_already_sorted(self):
        self.assertListEqual(
            quick_sort([1, 4]),
            [1, 4])

    def test_n_is_4(self):
        self.assertListEqual(
            quick_sort([7, 2, 5, 1]),
            [1, 2, 5, 7])

    def test_n_is_5(self):
        self.assertListEqual(
            quick_sort([7, 2, 4, 5, 1]),
            [1, 2, 4, 5, 7])

    def test_n_is_8(self):
        self.assertListEqual(
            quick_sort([7, 2, 5, 1, 3, 101, 50, 45]),
            [1, 2, 3, 5, 7, 45, 50, 101])

    def test_n_is_10(self):
        self.assertListEqual(
            quick_sort([7, 2, 4, 5, 1, 8, 3, 9, 10, 6]),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_everything_above_pivot(self):
        self.assertListEqual(
            quick_sort([0, 2, 4, 5, 1, 8, 3, 9, 10, 6]),
            [0, 1, 2, 3, 4, 5, 6, 8, 9, 10])

    def test_everything_below_pivot(self):
        self.assertListEqual(
            quick_sort([100, 2, 4, 5, 1, 8, 3, 9, 10, 6]),
            [1, 2, 3, 4, 5, 6, 8, 9, 10, 100])


if __name__ == "__main__":
    unittest.main()

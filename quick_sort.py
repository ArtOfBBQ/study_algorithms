""" QuickSort algorithm illustrated in python.
"""

import unittest

from math import floor


work_done = 0


def reset_work_done():

    global work_done
    work_done = 0

    return


def get_median_3_i(x: list) -> int:
    """ Find index of the median of the leftmost, rightmost, and middle value of an array.

    Example: median is in index 1 of input list
        >>> get_median_3_i([3, 5, 6])
        1
    """

    leftmost = x[0]
    middle = x[floor((len(x)-0.01) / 2)]
    rightmost = x[len(x)-1]

    if (
      leftmost <= middle <= rightmost or
      leftmost >= middle >= rightmost):
        pivot_i = floor((len(x)-0.01) / 2)
    elif (
      middle <= leftmost <= rightmost or
      middle >= leftmost >= rightmost):
        pivot_i = 0
    elif (
      middle <= rightmost <= leftmost or
      middle >= rightmost >= leftmost):
        pivot_i = len(x)-1
    else:
        raise AssertionError("Impossible median case")

    return pivot_i


def quick_sort(x: list, pivot_choice: str = "leftmost") -> list:
    """ Sort a list of numbers.

    Please pass "leftmost", "rightmost", or "median 3" to the pivot_choice parameter.

    Example:
      >>> quick_sort([3, 8, 2, 5, 1, 4, 7, 6])
      [1, 2, 3, 4, 5, 6, 7, 8]
    """

    global work_done
    work_done += max(len(x)-1, 0)

    # print("Current input:" + str(x) + " - Work done so far: " + str(work_done))

    if len(x) < 2:
        return x

    # Pre-processing step:
    # Choose pivot and move it to index 0 here
    if pivot_choice == "leftmost":
        pivot_i = 0
    elif pivot_choice == "rightmost":
        pivot_i = len(x)-1
    elif pivot_choice == "median 3":
        pivot_i = get_median_3_i(x)
    else:
        raise ValueError("Please pass 'leftmost', 'rightmost' or 'median 3' to pivot_choice param.")
    x[0], x[pivot_i] = x[pivot_i], x[0]

    last_below_pivot_i = 1
    for unseen_i in range(1, len(x)):
        if x[unseen_i] < x[0]:
            x[last_below_pivot_i], x[unseen_i] = x[unseen_i], x[last_below_pivot_i]
            last_below_pivot_i += 1

    # Swap pivot to the middle
    x[last_below_pivot_i-1], x[0] = x[0], x[last_below_pivot_i-1]

    # Identify the chunks
    smaller_chunk = x[:last_below_pivot_i-1]
    assert isinstance(smaller_chunk, list)
    pivot = x[last_below_pivot_i-1]
    bigger_chunk = x[last_below_pivot_i:]
    assert isinstance(bigger_chunk, list)

    return quick_sort(smaller_chunk, pivot_choice) + [pivot] + quick_sort(bigger_chunk, pivot_choice)


class TestQuickSort(unittest.TestCase):
    def setUp(self):
        pass

    def test_n_is_2(self):
        self.assertListEqual(
            quick_sort([7, 2], "median 3"),
            [2, 7])

    def test_n_is_2_already_sorted(self):
        self.assertListEqual(
            quick_sort([1, 4], "median 3"),
            [1, 4])

    def test_n_is_4(self):
        self.assertListEqual(
            quick_sort([7, 2, 5, 1]),
            [1, 2, 5, 7])

    def test_n_is_5(self):
        self.assertListEqual(
            quick_sort([7, 2, 4, 5, 1], "median 3"),
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
            quick_sort([0, 2, 4, 5, 1, 8, 3, 9, 10, 6], "rightmost"),
            [0, 1, 2, 3, 4, 5, 6, 8, 9, 10])

    def test_everything_below_pivot(self):
        self.assertListEqual(
            quick_sort([100, 2, 4, 5, 1, 8, 3, 9, 10, 6]),
            [1, 2, 3, 4, 5, 6, 8, 9, 10, 100])


class TestFindMedian3(unittest.TestCase):

    def test_n_is_5(self):
        self.assertEqual(
            get_median_3_i([1, 2, 3, 4, 5]),
            2)

    def test_n_is_6(self):
        self.assertEqual(
            get_median_3_i([1, 2, 3, 4, 5, 20]),
            2)

    def test_n_is_6_right_most_median(self):
        self.assertEqual(
            get_median_3_i([1, 2, 20, 4, 5, 3]),
            5)

    def test_n_is_6_left_most_median(self):
        self.assertEqual(
            get_median_3_i([3, 2, 20, 4, 5, 1]),
            0)


if __name__ == "__main__":
    unittest.main()

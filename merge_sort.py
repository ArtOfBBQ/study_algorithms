""" Merge sort algorithm illustrated in python.
"""

import unittest


def merge_sort(x: list) -> list:
    """ Sort a list of numbers.

    Example:
      >>> merge_sort([3, 2, 1, 0, 4, 5])
      [0, 1, 2, 3, 4, 5]
    """

    input_length = len(x)

    break_point = input_length // 2

    first_slice = x[:break_point]
    second_slice = x[break_point:]

    if input_length > 2:
        first_slice = merge_sort(first_slice)
        second_slice = merge_sort(second_slice)

    return merge(first_slice, second_slice)


def merge(array1: list, array2: list) -> list:
    """ Merge 2 sorted lists into 1 large sorted list.

    The arguments array1 and array2 must already be sorted.

    Example:
      >>> merge([1, 2, 3], [0, 4, 5])
      [0, 1, 2, 3, 4, 5]
    """

    i = 0
    y = 0
    output = []

    while i < len(array1) and y < len(array2):
        if array1[i] < array2[y]:
            output.append(array1[i])
            i += 1
        else:
            output.append(array2[y])
            y += 1

    # One of the two inputs is now exhausted.
    # We can simply append the other input's remaining values
    if i < len(array1):
        output += array1[i:]
    else:
        output += array2[y:]

    return output


class TestMergeSort(unittest.TestCase):
    def setUp(self):
        pass

    def test_n_is_2(self):
        self.assertListEqual(
            merge_sort([7, 2]),
            [2, 7])

    def test_n_is_2_already_sorted(self):
        self.assertListEqual(
            merge_sort([1, 4]),
            [1, 4])

    def test_n_is_4(self):
        self.assertListEqual(
            merge_sort([7, 2, 5, 1]),
            [1, 2, 5, 7])

    def test_n_is_5(self):
        self.assertListEqual(
            merge_sort([7, 2, 4, 5, 1]),
            [1, 2, 4, 5, 7])

    def test_n_is_8(self):
        self.assertListEqual(
            merge_sort([7, 2, 5, 1, 3, 101, 50, 45]),
            [1, 2, 3, 5, 7, 45, 50, 101])

    def test_n_is_10(self):
        self.assertListEqual(
            merge_sort([7, 2, 4, 5, 1, 8, 3, 9, 10, 6]),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


class TestMergeStep(unittest.TestCase):
    def setUp(self):
        pass

    def test_merge_empty_inputs(self):
        self.assertListEqual(
            merge([], []),
            [])

    def test_merge_length_2_lists(self):
        self.assertListEqual(
            merge([2, 4], [1, 3]),
            [1, 2, 3, 4])

    def test_merge_length_4_lists(self):
        self.assertListEqual(
            merge([2, 4, 5, 6], [1, 3, 7, 9]),
            [1, 2, 3, 4, 5, 6, 7, 9])


if __name__ == "__main__":
    unittest.main()

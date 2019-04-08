""" This is another algorithm from the coursera course.

It's very similar to the merge sort algorithm (see merge_sort.py).

We'll be counting the number of "inversions" in a list of numbers. E.g. in [1, 3, 2, 5] the 3 and 2 are an inversion
because 3 is bigger than 2 even though it appears earlier in the list.

In [1, 5, 3, 4, 2, 6] the inversions are (5, 3), (5, 4), (5, 2), (3, 4), (3, 2), (4, 2)
"""

import unittest
from typing import Tuple


def count_inversions(x: list) -> Tuple[list, int]:
    """ Count the number of inversions in a list of numbers.

    Example:
      >>> count_inversions([1, 4, 3, 2, 5])
      3
    """

    input_length = len(x)

    break_point = input_length // 2

    first_slice = x[:break_point]
    second_slice = x[break_point:]
    local_inversions = 0

    if input_length > 2:
        first_slice, first_slice_inversions = count_inversions(first_slice)
        second_slice, second_slice_inversions = count_inversions(second_slice)
        local_inversions = first_slice_inversions + second_slice_inversions

    combined_slices, split_inversions = count_split_inversions_and_merge(first_slice, second_slice)

    return combined_slices, split_inversions + local_inversions


def count_split_inversions_and_merge(array1: list, array2: list) -> Tuple[list, int]:
    """ Merge 2 sorted lists into 1 large sorted list, and track the number of split inversions.

    The arguments array1 and array2 must already be sorted.

    Example:
      >>> merge([1, 2, 3], [0, 4, 5])
      [0, 1, 2, 3, 4, 5]
    """

    i = 0
    y = 0
    output = []
    split_inversion_count = 0

    while i < len(array1) and y < len(array2):
        if array1[i] < array2[y]:
            output.append(array1[i])
            i += 1
        else:
            output.append(array2[y])
            y += 1
            split_inversion_count += len(array1) - i

    # One of the two inputs is now exhausted.
    # We can simply append the other input's remaining values
    if i < len(array1):
        output += array1[i:]
    else:
        output += array2[y:]

    return output, split_inversion_count


class TestCountInversions(unittest.TestCase):
    def setUp(self):
        pass

    def test_n_is_2_sorting(self):
        self.assertListEqual(
            count_inversions([7, 2])[0],
            [2, 7])

    def test_n_is_2_inversions(self):
        self.assertEqual(
            count_inversions([7, 2])[1],
            1)

    def test_n_is_2_already_sorted(self):
        self.assertListEqual(
            count_inversions([1, 4])[0],
            [1, 4])

    def test_n_is_4_sorting(self):
        self.assertListEqual(
            count_inversions([7, 2, 5, 1])[0],
            [1, 2, 5, 7])

    def test_n_is_4_inversions(self):
        self.assertEqual(
            count_inversions([7, 2, 5, 1])[1],
            5)

    def test_n_is_5_sorting(self):
        self.assertListEqual(
            count_inversions([1, 2, 3, 5, 4])[0],
            [1, 2, 3, 4, 5])

    def test_n_is_5_inversions(self):
        self.assertEqual(
            count_inversions([1, 2, 3, 5, 4])[1],
            1)

    def test_n_is_8_sorting(self):
        self.assertListEqual(
            count_inversions([7, 2, 5, 1, 8, 6, 3, 4])[0],
            [1, 2, 3, 4, 5, 6, 7, 8])

    def test_n_is_8_inversions(self):
        self.assertEqual(
            count_inversions([7, 2, 5, 1, 8, 6, 3, 4])[1],
            15)


class TestCountSplitInversionsAndMerge(unittest.TestCase):
    def setUp(self):
        pass

    def test_merge_empty_inputs(self):
        self.assertListEqual(
            count_split_inversions_and_merge([], [])[0],
            [])

    def test_merge_1_and_1_inputs(self):
        self.assertListEqual(
            count_split_inversions_and_merge([5], [4])[0],
            [4, 5])

    def test_count_inversions_for_1_and_1_inputs(self):
        self.assertEqual(
            count_split_inversions_and_merge([5], [4])[1],
            1)

    def test_merge_2_and_2_inputs(self):
        self.assertListEqual(
            count_split_inversions_and_merge([2, 4], [3, 5])[0],
            [2, 3, 4, 5])

    def test_count_inversions_for_2_and_2_inputs(self):
        self.assertEqual(
            count_split_inversions_and_merge([2, 4], [3, 5])[1],
            1)

    def test_merge_2_and_2_inputs_2(self):
        self.assertListEqual(
            count_split_inversions_and_merge([4, 5], [2, 3])[0],
            [2, 3, 4, 5])

    def test_count_inversions_for_2_and_2_inputs_2(self):
        self.assertEqual(
            count_split_inversions_and_merge([4, 5], [2, 3])[1],
            4)

    def test_merge_4_and_4_inputs(self):
        self.assertListEqual(
            count_split_inversions_and_merge([2, 3, 4, 5], [1, 6, 7, 8])[0],
            [1, 2, 3, 4, 5, 6, 7, 8])

    def test_count_inversions_for_4_and_4_inputs(self):
        self.assertEqual(
            count_split_inversions_and_merge([2, 3, 4, 5], [1, 6, 7, 8])[1],
            4)

    def test_merge_4_and_4_inputs_2(self):
        self.assertListEqual(
            count_split_inversions_and_merge([2, 4, 5, 6], [1, 3, 7, 8])[0],
            [1, 2, 3, 4, 5, 6, 7, 8])

    def test_count_inversions_for_4_and_4_inputs_2(self):
        self.assertEqual(
            count_split_inversions_and_merge([2, 4, 5, 6], [1, 3, 7, 8])[1],
            7)


if __name__ == "__main__":
    unittest.main()

""" "Karatsuba multiplication" implemented in Python.

https://en.wikipedia.org/wiki/Karatsuba_algorithm
"""


import unittest

from math import log10


def karatsuba(x, y):
    """ Multiply with Karatsuba's algorithm.

    Example: multiplying 22 by 18.
      >>> karatsuba(2, 4)
      8
    """

    if x < 10 or y < 10:
        return x * y

    # Number of 0's to pad step 1 with later
    modifier_1 = max(int(log10(x) + 1), int(log10(y) + 1))
    # If the modifier is odd, it needs to be adjusted
    if modifier_1 % 2 != 0:
        modifier_1 -= 1

    # Number of 0's of padding for step3 later
    modifier_2 = int(modifier_1 / 2)

    a, b = divmod(x, 10 ** modifier_2)
    c, d = divmod(y, 10 ** modifier_2)

    step_1 = karatsuba(a, c)
    step_2 = karatsuba(b, d)
    step_3 = karatsuba((a + b), (c + d)) - step_1 - step_2

    return (step_1 * (10 ** modifier_1)) + step_2 + (step_3 * (10 ** modifier_2))


class TestKaratsuba(unittest.TestCase):
    def setUp(self):
        pass

    def test_2_times_2(self):
        self.assertEqual(
            karatsuba(2, 2),
            4)

    def test_24_times_2(self):
        self.assertEqual(
            karatsuba(24, 2),
            48)

    def test_35_times_68(self):
        self.assertEqual(
            karatsuba(35, 68),
            2380)

    def test_1001_times_54321(self):
        self.assertEqual(
            karatsuba(1001, 54321),
            54375321)

    def test_123456789_times_54321(self):
        self.assertEqual(
            karatsuba(123456789, 54321),
            6706296235269)

    def test_654798794654_times_456489794321(self):
        self.assertEqual(
            karatsuba(654798794654, 456489794321),
            298908967093243174359934)


if __name__=="__main__":
    unittest.main()

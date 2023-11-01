#!/usr/bin/python3
""" unittest for maxinteger """

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ test maxinteger """

    def test_ordered_list(self):
        """ Test an ordered list of integer """
        self.assertEqual(max_integer([1, 2, 3, 4]),4)
    
    def test_unordered_list(self):
        """ Test unordered list of integer """
        self.assertEqual(max_integer([1, 4, 2 ,3]), 4)

    def test_rev_order_list(self):
        """ Test list in reverse order """
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """ Test an empty list """
        self.assertEqual(max_integer([]), None)

    def test_single_elem(self):
        """ Test a single element list """
        self.assertEqual(max_integer([2]), 2)

    def test_single_neg_elem(self):
        """Test one negative num """
        self.assertEqual(max_integer([-2]), -2)


if __name__ == '__main__':
    unittest.main()
        
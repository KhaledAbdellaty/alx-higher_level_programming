#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
      def test_empty_list(self):
          self.assertIsNone(max_integer([]))

      def test_positive_numbers(self):
          res = max_integer([1, 2, 3, 4, 5])
          self.assertEqual(res, 5)

      def test_negative_numbers(self):
          res = max_integer([-1, -2, -3, -4, -5])
          self.assertEqual(res, -1)

      def test_mixed_numbers(self):
          res = max_integer([-1, 5, -2, 7])
          self.assertEqual(res, 7)

      def test_dupicalted_numbers(self):
          self.assertEqual(max_integer([1, 2, 3, 3]), 3)

      def test_single_element(self):
          self.assertEqual(max_integer([1]), 1)

      def test_float_numbers(self):
          res = max_integer([1.15, 2.50, 1.90])
          self.assertEqual(res, 2.50)

if __name__ == "__main__":
    unittest.main()

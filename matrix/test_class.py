import unittest
from matrixclass import Matrix
from typing import List


#I took the more complicated functions in the code in  for my opinion... and on them, I did test#


class TestClass(unittest.TestCase):
    def setUp(self) -> None:
        self.matrix = Matrix(3, 3)

    # unittest for testing the comparison of an amount between two objects of matrix
    def test_compare_sum(self):
        expected_input: bool = self.matrix.compare_sum(self.matrix)
        expected_output: bool = True
        self.assertEqual(expected_input, expected_output)

    # unittest for testing a sub-matrix from a main matrix
    def test_get_submatrix(self):
        expected_input: List[List[int]] = self.matrix.get_submatrix(0, 1, 0, 2)
        expected_output: List[List[int]] = [[5, 5, 5], [5, 5, 5]]
        self.assertEqual(expected_input, expected_output)

    # unittest for testing the multiplication of a sub-matrix by a given value from a main matrix
    def test_get_multiplied_submatrix(self):
        expected_input: List[List[int]] = self.matrix.get_multiplied_submatrix(0, 1, 0, 2, 10)
        expected_output: List[List[int]] = [[50, 50, 50], [50, 50, 50]]
        self.assertEqual(expected_input, expected_output)


if __name__ == "__main__":
    unittest.main()

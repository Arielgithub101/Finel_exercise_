import numpy as np
from numpy import ndarray


class MatrixClass2:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.matrix = np.zeros([self.row, self.col], dtype=int)

    def print_matrix(self) -> ndarray:
        return self.matrix

    def get_valu_at(self, row: int, col: int) -> int:
        return self.matrix[row][col]

    def sum_row(self, row: int) -> int:
        return self.matrix.sum(axis=1)[row - 1]

    def sum_col(self, col: int) -> int:
        return self.matrix.sum(axis=0)[col - 1]

    def compers_sum(self, matrix_check: list[list]) -> bool:
        sum1: int = 0
        for row in range(len(matrix_check)):
            for colum in range(len(matrix_check[0])):
                sum1 += matrix_check[row][colum]
        return self.matrix.sum() == sum1

    def __getitem__(self, item):
        return self.matrix[item]

    def __len__(self):
        return len(self.matrix)

    #
    def __add__(self, other: 'MatrixClass2'):
        new_mat = MatrixClass2(self.row,self.col)
        new_mat.matrix = np.add(self.matrix, other.matrix)
        return new_mat.print_matrix()

    def __sub__(self, other: 'MatrixClass2'):
        new_mat = MatrixClass2(self.row, self.col)
        new_mat.matrix = np.subtract(self.matrix, other.matrix)
        return new_mat.print_matrix()

    def __mul__(self, scaler: int):
        new_mat = MatrixClass2(self.row, self.col)
        new_mat.matrix = np.multiply(self.matrix,scaler)
        return new_mat.print_matrix()


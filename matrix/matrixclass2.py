import  numpy as np
class MatrixClass2:
    def __init__(self, row: int, col: int):
        self.matrix = np.zeros([row, col], dtype = int)

    def print_matrix(self) -> None:
        for i in range(len(self.matrix)):
            print(self.matrix[i])

    def get_valu_at(self, row: int, col: int) -> int:
        return self.matrix[row][col]

    def sum_row(self, row: int) -> int:
        return self.matrix.sum(axis=1)[row-1]

    def sum_colum(self, col: int) -> int:
        return self.matrix.sum(axis=0)[col-1]

    def compers_sum(self, matrix_check:'MatrixClass2') -> bool:
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
    # def __add__(self, other: 'Matrix'):
    #     result = [[0 for i in range(len(self.matrix))] for j in range(len(self.matrix[0]))]
    #     if isinstance(other, Matrix):
    #         for i in range(len(self.matrix)):
    #             for j in range(len(self.matrix[0])):
    #                 result[i][j] = self.matrix[i][j] + other[i][j]
    #         return result
    #     else:
    #         raise Exception("not a matrix class object")
    #
    # def __sub__(self, other: 'Matrix'):
    #     result = [[0 for i in range(len(self.matrix))] for j in range(len(self.matrix[0]))]
    #     if isinstance(other, Matrix):
    #         for i in range(len(self.matrix)):
    #             for j in range(len(self.matrix[0])):
    #                 result[i][j] = self.matrix[i][j] - other[i][j]
    #         return result
    #     else:
    #         raise Exception("not a matrix class object")
    #
    # def __mul__(self, other: 'Matrix'):
    #     result = [[0 for i in range(len(self.matrix))] for j in range(len(self.matrix[0]))]
    #     if isinstance(other, Matrix):
    #         for i in range(len(self.matrix)):
    #             for j in range(len(self.matrix[0])):
    #                 result[i][j] = self.matrix[i][j] * other[i][j]
    #         return result
    #     else:
    #         raise Exception("not a matrix class object")
    #
    #
    #



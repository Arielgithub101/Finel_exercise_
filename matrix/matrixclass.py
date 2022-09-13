from typing import List, Any


class Matrix:
    def __init__(self, row: int, col: int):
        self.matrix = [[5 for j in range(col)] for i in range(row)]

    def __getitem__(self, item: int):
        return self.matrix[item]

    def __add__(self, matrix_obj: 'Matrix') -> 'Matrix':
        if isinstance(matrix_obj, Matrix):
            if len(matrix_obj.matrix) != len(self.matrix) or len(matrix_obj.matrix[0]) != len(self.matrix[0]):
                raise ValueError("length or width of matrix obj is Incompatible/out of range")
            result = Matrix(len(self.matrix), len(self.matrix[0]))
            if isinstance(matrix_obj, Matrix):
                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[0])):
                        result[i][j] = self.matrix[i][j] + matrix_obj[i][j]
                return result
            else:
                raise Exception("not a matrix class object")
        else:
            print('not Matrix obj, no adding was made.')
            return matrix_obj

    def __sub__(self, matrix_obj: 'Matrix') -> 'Matrix':
        if isinstance(matrix_obj, Matrix):
            if len(matrix_obj.matrix) != len(self.matrix) or len(matrix_obj.matrix[0]) != len(self.matrix[0]):
                raise ValueError("length/width of the matrix obj is Incompatible")
            result = Matrix(len(self.matrix), len(self.matrix[0]))
            if isinstance(matrix_obj, Matrix):
                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[0])):
                        result[i][j] = self.matrix[i][j] - matrix_obj[i][j]
                return result
            else:
                raise Exception("not a matrix class object")
        else:
            print('not Matrix obj, no substracting was made.')
            return matrix_obj

    def __mul__(self, scaler: int) -> 'Matrix':
        result = Matrix(len(self.matrix), len(self.matrix[0]))
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result[i][j] = self.matrix[i][j] * scaler
        return result

    def __eq__(self, other:'Matrix'):
        if isinstance(other, Matrix):
            for i in range(len(self.matrix)):
                if self.matrix[i] != other[i]:
                    return False
            return True
        return False

    def print_matrix(self) -> None:
        for i in range(len(self.matrix)):
            print(self.matrix[i])

    def get_value_at(self, row: int, col: int) -> int:
        return self.matrix[row][col]

    def sum_row(self, row: int) -> int:
        return sum(self.matrix[row])

    def sum_col(self, col: int) -> int:
        sum_item_in_col: int = 0
        for row in range(len(self.matrix)):
            sum_item_in_col += self.matrix[row][col]
        return sum_item_in_col

    def compare_sum(self, matrix_obj: 'Matrix') -> bool:
        sum1: int = 0
        sum2: int = 0
        for i in range(len(self.matrix)):
            sum1 += self.sum_row(i)
        for i in range(len(matrix_obj.matrix)):
            sum2 += matrix_obj.sum_row(i)
        return sum1 == sum2

    def get_submatrix(self, row_start: int, row_end: int, col_start: int, col_end: int) -> List[List[int]]:
        if row_start < 0 or row_end >= len(self.matrix) or col_start < 0 or col_end >= len(self.matrix[0]):
            raise ValueError("Date provided incorect, list index out of range")
        return [[self.matrix[i][j] for j in range(col_start, col_end + 1)] for i in range(row_start, row_end + 1)]

    def get_multiplied_row(self, index_row: int, scaler: int)-> List[int]:
        return list(map(lambda x: x * scaler, self.matrix[index_row]))

    def get_multiplied_submatrix(self, row_start: int, row_end: int, col_start: int, col_end: int, scaler: int) -> List[List[int]]:
        new_mat = self.get_submatrix(row_start, row_end, col_start, col_end)
        for i in range(len(new_mat)):
            new_mat[i] = self.get_multiplied_row(i, scaler)
        return new_mat

class Matrix:
    def __init__(self, row: int, col: int):
        self.matrix = [[4 for j in range(row)] for i in range(col)]

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

    def compers_sum(self, matrix_check: list[list]) -> bool:
        sum1: int = 0
        sum2: int = 0
        for row in range(len(matrix_check)):
            for colum in range(len(matrix_check[0])):
                sum1 += matrix_check[row][colum]
        for row in range(len(self.matrix)):
            for colum in range(len(self.matrix[0])):
                sum2 += self.matrix[row][colum]
        return sum1 == sum2

    def get_submatrix(self, row_start: int, row_end: int, col_start: int, col_end: int) -> list[list[any]]:
        result: list[list[int]] = []
        for i in range(row_start, row_end + 1):
            sub_result: list[int] = []
            for j in range(col_start, col_end + 1):
                sub_result.append(self.matrix[i][j])
            result.append(sub_result)
        return result

    def get_multiplied_row(self, index_row: int, scaler: int):
        return list(map(lambda x: x * scaler, self.matrix[index_row]))

    def get_multiplied_submatrix(self,row_start: int, row_end: int, col_start: int, col_end: int,scaler:int)->list[list[int]]:
        new_mat = self.get_submatrix(row_start, row_end, col_start, col_end)
        for i in range(len(new_mat)):
            for j in range(len(new_mat[0])):
                new_mat[i][j] = new_mat[i][j] * scaler
        return new_mat

    def __getitem__(self, item):
        return self.matrix[item]

    def __add__(self, other: 'Matrix'):
        result = [[0 for i in range(len(self.matrix))] for j in range(len(self.matrix[0]))]
        if isinstance(other, Matrix):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    result[i][j] = self.matrix[i][j] + other[i][j]
            return result
        else:
            raise Exception("not a matrix class object")

    def __sub__(self, other: 'Matrix'):
        result = [[0 for i in range(len(self.matrix))] for j in range(len(self.matrix[0]))]
        if isinstance(other, Matrix):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    result[i][j] = self.matrix[i][j] - other[i][j]
            return result
        else:
            raise Exception("not a matrix class object")

    def __mul__(self, scaler: int):
        result = [[0 for i in range(len(self.matrix))] for j in range(len(self.matrix[0]))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                result[i][j] = self.matrix[i][j] * scaler
        return result

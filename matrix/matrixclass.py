class Matrix:
    def __init__(self, row: int, col: int):
        self.matrix = [[1 for j in range(row)] for i in range(col)]

    def print_matrix(self) -> None:
        for i in range(len(self.matrix)):
            print(self.matrix[i])

    def get_valu_at(self, row: int, col: int) -> int:
        return self.matrix[row][col]

    def sum_row(self, row: int) -> int:
        sum_item_in_row: int = 0
        for i in self.matrix[row - 1]:
            sum_item_in_row += i
        return sum_item_in_row

    def sum_colum(self, col: int) -> int:
        sum_item_in_col: int = 0
        for row in range(len(self.matrix)):
            sum_item_in_col += self.matrix[row][col - 1]
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

    def __mul__(self, other: 'Matrix'):
        result = [[0 for i in range(len(self.matrix))] for j in range(len(self.matrix[0]))]
        if isinstance(other, Matrix):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    result[i][j] = self.matrix[i][j] * other[i][j]
            return result
        else:
            raise Exception("not a matrix class object")

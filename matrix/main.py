# class Matrix:
#     def __init__(self, n, m):
#         self.matrix = self.get_matrix(n, m)
#
#     def get_matrix(self, n, m):
#         num = 1
#         matrix = [[None for j in range(m)] for i in range(n)]
#         for i in range(len(matrix)):
#             for j in range(len(matrix[i])):
#                 matrix[i][j] = num
#                 num += 1
#         return matrix
#
#     def get_readable_matrix_string(self, matrix):
#         strings = []
#         for row in matrix:
#             strings.append(str(row))
#         return '\n'.join(strings)
#
#     def __str__(self):
#         return self.get_readable_matrix_string(self.matrix)
#
#     def __len__(self):
#         return len(self.matrix)
#
#     def __getitem__(self, item):
#         return self.matrix[item]
#
#     def getElement(self, i, j):
#         return self.matrix[i - 1][j - 1]
#
#     def setElement(self, i, j, element):
#         self.matrix[i - 1][j - 1] = element
#
#     def transpose(self, matrix):
#         return [list(i) for i in zip(*matrix)]
#
#     def getTranspose(self):
#         return self.get_readable_matrix_string(self.transpose(self.matrix))
#
#     def doTranspose(self):
#         self.matrix = self.transpose(self.matrix)
#
#     def multiply(self, matrix):
#         result = [[0 for j in range(len(matrix[i]))] for i in range(len(self.matrix))]
#         for i in range(len(self.matrix)):
#             for j in range(len(matrix[0])):
#                 for k in range(len(matrix)):
#                     result[i][j] += self.matrix[i][k] * matrix[k][j]
#         return result
#
#     def getMultiply(self, matrix):
#         return self.get_readable_matrix_string(self.multiply(matrix))
#
#     def __mul__(self, other):
#         if isinstance(other, Matrix):
#             return self.get_readable_matrix_string(self.multiply(other))
#         return self.get_readable_matrix_string([[num * other for num in row] for row in self.matrix])
import numpy as np

from matrixclass import Matrix
from matrixclass2 import MatrixClass2

a = MatrixClass2(3,3)
c = MatrixClass2(3,3)
b = np.array([[1,2],[3,4]])
# print(a.print_matrix())
print(b[1][1])
print(a.compers_sum(c))
#print(b.sum(axis=1)[0])




# m1 = Matrix(2, 3)
# print(m1.get_matrix(4,4))
# print(m1.get_readable_matrix_string(m1))
# a = Matrix(4,4)
# ab = MatrixClass2(4,4)
# b = Matrix(4,4)
# print(a.print_matrix())
#
#
#
# s = [ [1,1,1],
#       [1,1,1],
#       [1,1,1]]
#
#
# print(a.compers_sum(s))
# print(a.sum_colum(2))
# print(a*b)
# print(a-b)
# print(a+6)
# print(a.print_matrix())
#
# s = [[1,2,3,4],
#      [1,2,3],
#      [1,2,3]]
#
# print(len(s[0]))
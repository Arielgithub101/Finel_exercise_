import numpy as np
from matrixclass import Matrix
from matrixclass2 import MatrixClass2

a = MatrixClass2(3,3)
b = MatrixClass2(3,3)
x = [[1,2,3],[4,5,6]]

print(a.print_matrix())
print(a.sum_row(2))
print(a.sum_col(2))
print(a.compers_sum(x))

print('-----------------')
print(a+b,)
print('-----------------')
print(a-b,'!here 2')
print('-----------------')
print(a*5, '!here 3')
print('-----------------')



c = Matrix(3,3)
d = Matrix(3,3)
y = [[1,2,3],[4,5,6]]

print(c.print_matrix())
print(c.sum_row(2))
print(c.sum_col(2))
print(c.compers_sum(y))

print('-----------------')
print(a+b)
print('-----------------')
print(a-b)
print('-----------------')
print(a*5)
print('-----------------')



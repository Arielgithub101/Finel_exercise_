import numpy as np
from matrixclass import Matrix
from matrixclass2 import MatrixClass2

#
# a = MatrixClass2(3,3)
# b = MatrixClass2(3,3)
# x = [[1,2,3],[4,5,6]]
#
# print(a.print_matrix())
# print(a.sum_row(2))
# print(a.sum_col(2))
# print(a.compers_sum(x))
#
# print('-----------------')
# print(a+b,)
# print('-----------------')
# print(a-b,'!here 2')
# print('-----------------')
# print(a*5, '!here 3')
# print('-----------------')
#


c = Matrix(3, 3)
d = Matrix(3, 3)
p = Matrix(2, 3)
y = [[5, 5, 5],
     [5, 5, 5],
     [5, 5, 5]
     ]

print(c.print_matrix())
print(p.print_matrix())
print(c.sum_row(2))
print(c.sum_col(1))
print(c.compare_sum(p))
print(c.get_submatrix(0, 1, 0, 2))
print(c.get_multiplied_row(0,10))
print(c.get_multiplied_submatrix(0, 1, 0, 2,10))


print('-----------------')
obj1 = c + d
obj1.print_matrix()
print('-----------------')
obj2 = c - d
obj2.print_matrix()
print('-----------------')
obj3 = c * 5
obj3.print_matrix()
print('-----------------')
print(c == p)

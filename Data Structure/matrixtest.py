
from numpy import *

m1 = matrix('1 2 3 ; 4 5 6 ; 7 8 9')
m2 = matrix('3 2 1 ; 5 4 6 ; 9 8 7')

print('matrix one is\n {} \n and matrix two is \n{} '.format(m1,m2))

d = diagonal(m1)
d2 = diagonal(m2)

print('diagonal of this matrix one is {}'.format(d))
print('diagonal of this matrix two is {}'.format(d2))

print('addtion of two matrices ')

addmatrix = m1 + m2
multiplymatrix = m1 * m2

print(addmatrix)
print(multiplymatrix)

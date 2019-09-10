

from numpy import *

m1 = matrix('1,2,3;3,3,4;5,6,7')
m2 = matrix('3,2,4;6,7,8;1,4,3')
m3 = m1*m2

print(m3)

mat1 = array([
        [1,2,3],
        [3,4,5],
        [5,6,7]
])

mat2 = array([
        [3,2,4],
        [6,7,8],
        [1,4,3]
])

for i in mat1:
    for j in mat2:
        mat3 = mat1 * mat2


#print(mat3)

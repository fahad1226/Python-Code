import numpy as np
np_2d = np.array([
    [1,2,3,4,5,6],
    [5,6,7,8,9,9],
    [5,4,3,2,4,5]
])

print(np_2d)
print(np_2d.shape)

one = np_2d[0][3]
one_2 = np_2d[0:2]
print(one)
print(one_2)

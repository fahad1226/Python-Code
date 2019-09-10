
from numpy import *


arr1 = array([
    [1,2,3,4,54,34],
    [2,1,3,4,55,23]

])

arr2 = array([
    [3,3,4,3,4,2],
    [3,2,4,4,5,4]
])
print(arr1)
print(arr2)

add2dinemsionarraty = arr1 + arr2

print('addition of these two array is\n {}'.format(add2dinemsionarraty))


#convert these array into 1d array

flatarray = arr1.flatten()
print(flatarray,len(flatarray))

convertto3d = flatarray.reshape(6,2)

print(convertto3d)

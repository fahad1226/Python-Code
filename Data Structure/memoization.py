from array import *

#that recursive problem we solved using dynamic programming

A = array('i',[-1,-1,-1,-1,-1,-1,-1,-1])

A[0] = 0
A[1] = 1

for i in range(2,7):
    A[i] = A[i-2] + A[i-1]
    print(A[i],end=' ')

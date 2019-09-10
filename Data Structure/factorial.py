
from math import *

fact = 1

n = int(input('enter e number to find its factorial '))

for i in range(1,n+1):
    fact  *= i

print(fact)

cnt = len(str(abs(fact)))

print(cnt)

f = lambda a,b:a*b
res = f(2,3)

print(res)

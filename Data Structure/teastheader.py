
from header import *

#a,b = input().split()
#a = int(a)
#b= int(b)

a,b = list(map(int, input (). split ()))  #to take as much input you want

c = add(a,b)

d = subtract(a,b)

x,y = list(map(int,input('enter two value to multiplication ').split()))

e = multi(x,y)

print(c)
print(d)
print(e)

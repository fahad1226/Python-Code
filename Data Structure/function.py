

from math import *

#function 1
def fahad(x,y):

    z = x**y
    print(x ,' to the power ',y, ' is equal to',z)
    b = bin(x)
    print('binary of' ,x, 'is ',b)
    c = bin(y)
    print('binary of ',y, ' is ',c)
    sq = sqrt(x)
    print('square root of ',x,' is ','%.0f'%sq)
    print('addition of ',x,'and',y,'is equal to',x+y)
    print('and thats all ')

x = int(input('enter first value fahad '))
y = int(input('enter second value fahad '))
fahad(x,y);


#function 2

def Sup():
    print("Fahad?where are you,I've been looking for you last 4 hours,where have you been?" )

Sup();


#function 3

def magicalAdd(a,b):
    c = a+b
    d = a-b
    return c,d

x = int(input('enter first value fahad '))
y = int(input('enter second value fahad '))
res1,res2 = magicalAdd(x,y)

print(res1,res2)

#function 4



def position(name,age,gender):
    nm = name
    ag = age
    sx = gender
    print('name is ',nm,' Age is ',ag,' Sex is ',sx)


position(name='Fahad',age=21,gender='male');

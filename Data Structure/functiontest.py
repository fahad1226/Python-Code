from array import *

def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even+=1
        else:
            odd+=1
    return even,odd

#lst = [2,3,4,1,454,2,4,34342,42344,24,5,6,7,4,6,7]

lst = array('i',[])

n = int(input('enter length '))

for i in range(1,n):
    x = int(input('enter {}th value '.format(i)))
    lst.append(x)

even,odd = count(lst)

print("Even number is {} and Odd is {} ".format(even,odd))

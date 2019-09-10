
from array import *

#2D Array example

Temp = [[1,2,3,4],[4,5,6,7],[7,6,5,6]]

for each_element in Temp:

    for c in each_element:
        print(c,end=' ')


print()
print()
print('Tempareture of day 1')
print(Temp[0])

print('Tempareture of day 2')
print(Temp[1])

print('Tempareture of day 3')
print(Temp[2])

#insert another array at 3th index
Temp.insert(3,[2,3,12,3,3])
for each_element in Temp:
    print(each_element)


#update Array
print()
print()
Temp[2] = [1,2,3,3445,5,56]
for each_element in Temp:
    print(each_element)

#delete one array
print()
print()

del Temp[2]
for each_element in Temp:
    print(each_element)

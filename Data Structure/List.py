
list = ['Fahad','asif','ashim','Ishmam','Rasik','Faiz','Enan']

for each_element in list:

    print(each_element)

list2 = ['fahad',1226,'ashim',1224,'asif',1225]
print()
print()
print()
for each_element in list2:

    print(each_element)


print(list[0],list[1],list[2],list2[0],list2[1])

#delete from list

del list[-2]
del list[-1]
for each_element in list:

    print(each_element)

ln = len([1,2,3,4])
print(ln)
print([1,2,3,4,5]+[4,5,7,8]) #concatenation


print(['hii']*5)

print(1 in [1,2,3,45,5])


list.insert(0,'Fahad Bin Munir')
print(list[0])

for each_element in list:

    print(each_element)

from array import *
#array operation
arraname = array('i',[10,20,30,40,50,60])

for each_element in arraname:

    print(each_element)


print()
print()
print()
print()
print(arraname[2],arraname[3])
#insert value to the array

arraname.insert(4,100)
for each_element in arraname:

    print(each_element)
#delete value
arraname.remove(100)
print()
print()
print()
for each_element in arraname:

    print(each_element)

print(len(arraname))

#search value

search = arraname.index(10)
print('element is at {}th position '.format(search))

#update value

arraname[2] = 200
arraname[3] = 300

for each_element in arraname:
    print(each_element)

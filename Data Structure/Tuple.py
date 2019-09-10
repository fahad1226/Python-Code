
tuple1 = ('x','y','z',1,3,4,2)
tuple2 = ('programming','algorithm','data structure',80,90,77)


for each_element in tuple2:

    print(each_element)

#print(tuple2[1:5])

#update tuple2
for each_element in tuple2:

    print(each_element)

del tuple1 #tuple 1 was deleted
print(tuple1) #it will show a error msg which is tuple1 is not defined
print(type(tuple2))

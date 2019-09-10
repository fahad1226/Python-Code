
from numpy import *
"""
daily Tempareture of a week
[['Mon' '18' '20' '22' '17']
 ['Tue' '11' '18' '21' '18']
 ['Wed' '15' '21' '20' '19']
 ['Thu' '11' '20' '22' '21']
 ['Fri' '18' '17' '23' '22']
 ['Sat' '12' '22' '20' '18']
 ['Sun' '13' '15' '19' '16']]

 """



Tempareture = array([['mon',1,2,3,4],['Tue',4,5,6,7],['wed',3,2,4,5],['thu',2,1,4,5],['fri',4,3,2,1],['sat',4,3,5,4],['sun',4,3,21,4]])

#print(Tempareture)
m = reshape(Tempareture,(7,5))
print()
print()

print('Tempareture of wednesday is ',Tempareture[2])
print('Tempareture of friday is ',Tempareture[4])
print('Tempareture of saturday mornig is ',Tempareture[5][1])

print()
print()

m_r = append(Tempareture,[['Avg',12,15,13,11]],0)

for each_element in m_r:

    print(each_element)

#add new column
print()
print()
newcol = insert(Tempareture,[5],[[1],[2],[3],[4],[5],[6],[7]],1)

for each_element in newcol:

    print(each_element)


m = delete(Tempareture,[1],0)
print()
print()
for each_element in m:

    print(each_element)

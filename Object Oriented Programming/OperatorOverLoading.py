

class One:

    def __init__(self,m1,m2):

        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):

        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        m3 = One(m1,m2)
        return m3

    def __str__(self):

        return self.m1,self.m2

#ob1 = One(10,20)
#ob2 = One(30,40)
#ob3 = ob1+ob2
#print(ob3.m1,ob3.m2)
ob = One(10, 20)
print(ob.__str__())
class Five:

    def __init__(self,mem1,mem2,mem3):

        self.mem1 = mem1
        self.mem2 = mem2
        self.mem3 = mem3

    def __sub__(self,other):

        mem1 = self.mem1 - other.mem1
        mem2 = self.mem2 - other.mem2
        mem3 = self.mem3 - other.mem3
        res = Five(mem1,mem2,mem3)
        return res

    def __str__(self):

        return self.mem1,self.mem2,self.mem3






object = Five(600,100,150)
object2 = Five(400,500,600)
object3 = object - object2
print(object.__str__())
print(object2.__str__())
if object.mem1 and object.mem2 and object.mem3 > object2.mem1 and object2.mem2 and object2.mem3:

    print('Fuck,mem1 is greater')

else:

    print('No,mem2')


print(object3.mem1,object.mem2,object.mem3)

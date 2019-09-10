



class Student:

    University = 'Premier University'

    def __init__(self,m1,m2,m3,m4):

        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4

    def average(self):

        return (self.m1 + self.m2 + self.m3 + self.m4)/4

    def get_m1(self):

        return self.m1

    def set_m1(self,value):

        self.m1 = value

obj1 = Student(10,20,30,40)
obj2 = Student(30,40,34,56)
#print(obj1.getm1())
#d = obj2.average()
#print(d)



class Student:

    University = 'Premier University'
    def __init__(self,name,num1,num2,num3,num4,num5):

        self.name = name
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4
        self.num5 = num5
    def result(self):
        print('name of the stuident is ',self.name)
        print('Algorithm ',self.num1)
        print('Math ',self.num2)
        print('Programming ',self.num3)
        print('Databse ',self.num4)
        print('Data Structure ',self.num5)
        print('university is ',self.University)

    def average(self):
        return (self.num1+self.num2+self.num3+self.num4+self.num5)/5


    def compare(self,another):

        if object.average() > object2.average():
            print(object.name,'is better than ',object2.name)
        else:
            print(object2.name, 'is better than ',object.name)

object = Student('Fahad Bin Munir',70,80,89,77,80)
object2 = Student('Ashim Shill',90,90,80,99,90)
object.result()
print('average of',object.name, 'is ',object.average())
print()

object2.result()
print('average of',object2.name, 'is ',object2.average())

print(object.compare(object2))

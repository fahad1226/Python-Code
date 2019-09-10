
class Student:

    def __init__(self,name,age,address):

        self.name = name
        self.age = age
        self.address = address
        self.lap = self.Laptop()

    def information(self):
        print('name is ',self.name)
        print('age is ',self.age)
        print('address is ',self.address)
        self.lap.showinfo()

    class Laptop:

        def __init__(self):

            self.Brand = 'Hp'
            self.Ram = '8GB'
            self.CPU = 'Core i5'
            self.Hard_Disk = '1TB'

        def showinfo(self):

            print('name of the Laptop is ',self.Brand)
            print('It has {} Ram '.format(self.Ram))
            print('CPU is ',self.CPU)
            print('Hard Disk is ',self.Hard_Disk)


s1 = Student('Fahad Bin Munir',21,'Hathazari')
#print(s1.information())

lap1 = Student.Laptop()
#lap1.showinfo()
s1.information()

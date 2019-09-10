

class Person:

    def __init__(self,name,age,height,gpa,Id):

        self.name = name
        self.age = age
        self.height = height
        self.gpa = gpa
        self.Id = Id
        #self.lap = self.laptop()  show down,we can create object using that statment also,like object = outer_class.inner_class()

    def ShowDetails(self):

        print('Name is ',self.name)
        print('age is ',self.age)
        print('height of the person is ',self.height)
        print('his gpa is ',self.gpa)
        print('Id of the person is ',self.Id)



    class laptop:

        def __init__(self):

            self.brand = 'Hp'
            self.ram = '8gb'
            self.processor = 'i5'
            self.color = 'Black'


        def laptop_information(self):

            print('Brand is ',self.brand)
            print('Ram is ',self.ram)
            print('Processor is ',self.processor)
            print('color of this laptop is ',self.color)


ob = Person("Fahad",21,"5 feet 8 inch",3.78,1603110201226)
ob.ShowDetails()
ob2 = Person('X',20,'6 feet 2 inch',4,2323424)
# for inner class object

lap1 = Person.laptop()
lap2 = Person.laptop()
#lap1 = ob.lap
print()
print('see the what kind of laptop a student can get from this school')
print()
lap1.laptop_information()
#lap2 = ob2.lap
print(id(lap1))
print(id(ob))

print(id(lap2))
print()
print()
print('this is all about inner class practice,hope to see you again soon Fahad')
print('Love from Python')

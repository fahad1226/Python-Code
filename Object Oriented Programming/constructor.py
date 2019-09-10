

class We:

    semester = '4th'

    def __init__(self):

        self.name = "fahad"
        self.age = 21
        self.gpa = 3.78

    def myinformation(self):
        print('name is ',self.name)
        print('age is ',self.age)
        print('my gpa is ',self.gpa)

    def compare(c1,another):

        if c1.age == c2.age:
            return True
        else:
            return False

c1 = We()

c1.myinformation()
print(id(c1))

c2 = We()
c2.age = 20
c2.name = 'sinthi sen supti'
c2.gpa = 3.67
c2.myinformation()
print(id(c2))


print(c1.compare(c2))

print("fahad's semester",We.semester,"Sinthi's semester is also ",We.semester)

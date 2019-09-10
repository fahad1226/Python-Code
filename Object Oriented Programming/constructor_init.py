
class Computer:

    genere = 'Laptop'

    def __init__(self):

        self.name = "Hp"
        self.ram = 4
        self.harddisk = '1tb'

    @classmethod #this is called decoraters and this is a class method
    def info(cls):
        return cls.genere

    def printall(self):

        print(self.ram)
        print(self.name)
        print(self.harddisk)

    def compare(self,other): # instance method

        if self.ram == other.ram:

            return True
        else:
            return False

    @staticmethod
    def moja(): #this is static method

        print('python is okay')


com_1 = Computer()
com_2 = Computer()
#com_1.name = "asus"
#com_1.printall()
com_2.ram = 8
com_2.printall()
ob = Computer.info()
print(ob)

Computer.moja()

if com_1.compare(com_2):

    print('they are same')
else:
    print('they are different')

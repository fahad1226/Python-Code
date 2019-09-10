

class A:   # A class B or C class er methos or attribute use korte parbena

    def __init__(self):

        self.name = 'Fahad'
        self.age = 21
        self.University = 'Premier University'

    def showfun(self):

        print('Name is {}'.format(self.name))
        print('Age is ',self.age)
        print('University Name Is ',self.University)
        print('this is A class')


class B:

    id = 1226

    def showBclass(self):

        print('Name is ',self.name)
        print('id is ',self.id)
        print('this is B class')


class C(A,B):

    def showfuncforC(self):

        print('this is C class')
        print("Fahad's id is ",self.id)
        self.showfun()
        self.showBclass()


ob = C()
ob.showfuncforC()

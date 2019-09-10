
class A:

    def __init__(self,name,age,email):

        self.name = name
        self.age = age
        self.email = email

    def showinfo(self):

        print('Name is ',self.name)
        print('age is ',self.age)
        print('email is ',self.email)



class B(A):
    #pass
    def __init__(self):
        super().__init__('Fahad',10,'fahadbinmnr@gmail.com')
        print('Constructor of B class')
        self.showinfo()


ob = B()

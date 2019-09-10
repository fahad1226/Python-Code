

class Abbu:

    def phone(self):

        print('nokia 1110')

class Me(Abbu):

    def phone(self): #this method is override parents phone method func 
        print('samsung galaxy grand prime plus')



ob = Me()
ob.phone()

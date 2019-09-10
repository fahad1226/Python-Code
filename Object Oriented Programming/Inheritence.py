
class One:

    University = 'Premier University'

    def __init__(self,s_name,s_addrerss,s_Id,s_email):

        self.s_name = s_name
        self.address = s_addrerss
        self.s_Id = s_Id
        self.s_email = s_email


    def s_information(self):

        print('Name of the student is ',self.s_name)
        print('address is ',self.s_addrerss)
        print('Id is ',self.s_Id)
        print('Student email is ',self.s_email)
        print('University name is ',self.University)

    def showrealtion():

        print('ami Fahad')

class Two(One):

    def __init__(self,t_name,t_age,t_teach):

        self.t_age = t_age
        self.t_name = t_name
        self.t_teach = t_teach

    def t_information(self):
        print('teacher name is ',self.t_name)
        print('teacher age is ',self.t_age)
        print('Teacher teach us ',self.t_teach)
        print('Teacher from ',self.University)

#input from user
s1 = One.s_name = input('Enter Name ')
s2 = One.s_addrerss = input('Enter Student Address ')
s3 = One.s_Id = input('Enter Student Id ')
s4 = One.s_email = input('Enter Student email ')
first_object = One(s1,s2,s3,s4)
print(first_object.s_information())
secon_ob = Two('Minhaz',34,'programming & algorithm')
secon_ob.t_information()

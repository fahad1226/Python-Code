
class Employee:

    raise_amount = 1.04

    def __init__(self,first,last,pay,vacation):

        self.first = first
        self.last = last
        self.pay = pay
        self.vacation = vacation
        self.email = first + last + '@gmail.com'

    def fullname(self):

        return f'{self.first} {self.last}'


    def habijabai(self):

        return 'tumi ekta ajaira public'

    def apply_raise(self):

        self.pay = int(self.pay * Employee.raise_amount)



emp_1 = Employee('fahad','bin munir',50000,'40days')

print(emp_1.fullname())
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(Employee.raise_amount)
print(emp_1.raise_amount)

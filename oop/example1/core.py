class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(emp_1.first, emp_1.last)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Corey', 'sdasadasdasd', 50000)
# emp_2 = Employee()
print(emp_1.email)
print(emp_1.fullname())
print(Employee.fullname(emp_2))
# print(emp_2.email)

# emp_1.first = 'OK'
# emp_1.last = 'OK'
# emp_1.email = 'abc@gmail.com'
# emp_1.pay = 2000
#
# print(emp_1.pay)

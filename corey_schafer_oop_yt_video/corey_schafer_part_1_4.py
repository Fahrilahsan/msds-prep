import datetime


class Employee:

    num_of_emps = 0
    raise_amount = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@example.com'
        self.pay = pay
        
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())




# emp_1 = Employee('Fahril', 'Ahsan', 50000)
# emp_2 = Employee('Hasna', 'Fikriya', 60000)
dev_1 = Developer('Fahril', 'Ahsan', 50000, 'Python')
dev_2 = Developer('Hasna', 'Fikriya', 60000, 'Java')

mgr_1 = Manager('Siti', 'Aisyah', 90000, [dev_1])

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Jane-Mike-80000'

'''
# first, last, pay = emp_str_1.split('-')


# print(emp_1)
# print(emp_2)

# print(emp_1.email)
# print(emp_2.email)

# print('{} {}'.format(emp_1.first, emp_1.last))

# print(emp_1.fullname())
# emp_1.fullname()
# print(Employee.fullname(emp_1))

# print(Employee.raise_amount) --sama
# print(emp_1.raise_amount) --sama
# print(emp_2.raise_amount) --sama

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# emp_1.raise_amount

# print(Employee.num_of_emps)

# Employee.set_raise_amount(1.10)

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

# my_date = datetime.date(2024, 6, 10)

# print(Employee.is_workday(my_date))


'''

# print(help(Developer))

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_1.email)
# print(dev_1.prog_lang)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
print(mgr_1.email)
mgr_1.print_emps()







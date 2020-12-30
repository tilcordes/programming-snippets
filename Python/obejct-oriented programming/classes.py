class Employee:

    # class variable. All instances have the same class variables.
    raise_amount = 1.08
    number_of_employees = 0

    # executes when the class gets initiated
    def __init__(self, first, last, pay):

        # the __init__ mehtod contains instance variables. Instances variables gets created when the class gets initiated. They can be different for every instance.
        # self is written instead for the instance name(for example 'employee1')

        self.firstname = first
        self.lastname = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.number_of_employees += 1
    
    # function that is working with the instance of the class. It takes the instance as the first argument
    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    # function that is working with the instance of the class. It takes the instance as the first argument
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # function that only is working with the class and not with the instance. It takes the class as the first argument
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    #function that not works with the instance or the class. Should be used when the instance or the class is not needed
    @staticmethod
    def is_workday(day):
        if day.weekday == 6 or day.weekday == 7:
            return False
        return True


# creates an instance of the class
employee1 = Employee('Til', 'Cordes', 3000)
employee2 = Employee('Max', 'Mustermann', 5000)

# prints the variable 'email' of 'Employee'
print(employee1.email)
print(employee2.email + '\n')
print()

# executes the method 'fullname' of 'Employee'
print(employee1.fullname())
print(employee2.fullname())
print()

# Using not an instance but the class. The number of employess is the same for all instances.
print(Employee.number_of_employees)
print()

# the function 'set_raise_amount' changed the class variable 'raise_amount' for all instances
print(employee1.raise_amount)
print(employee2.raise_amount)
Employee.set_raise_amount(1.1)
print(employee1.raise_amount)
print(employee2.raise_amount)
print()

# executes the static function is_workday
import datetime
test_date = datetime.date(2020, 12, 30)
print(Employee.is_workday(test_date))

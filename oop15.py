class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return "I come to the office."

    def check_salary(self, days):
        return (self.salary * days)

    def __gt__(self, other):
        return (self.salary) > (other.salary)

    def __lt__(self, other):
        return (self.salary) < (other.salary)

    def __ge__(self, other):
        return (self.salary) >= (other.salary)

    def __le__(self, other):
        return (self.salary) <= (other.salary)


class Developer (Employee,):
    def work(self):
        return "I come to the office and start to coding."

    def __str__(self):
        name_class = str(self.__class__)
        return f"{name_class[17:-2]}:{self.name}"


class Recruiter (Employee,):
    def work(self):
        return "I come to the office and start to hiring."

    def __str__(self):
        name_class = str(self.__class__)
        return f"{name_class[17:-2]}:{self.name}"


michael = Developer("Michael", 1500)
print(michael)
print(michael.check_salary(10))

emma = Recruiter("Emma", 1000)
print(emma)
print(emma.check_salary(10))


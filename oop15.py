class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return "I come to the office."

    def check_salary(self, days):
        return (self.salary * days)


class Salary_comparison:
        def __init__(self, salary):
            self.salary = salary

            def __gt__(self, other):
                return (self) > (other)

            def __lt__(self, other):
                return (self) < (other)

            def __ge__(self, other):
                return (self) >= (other)

            def __le__(self, other):
                return (self) <= (other)

class Developer (Employee, Salary_comparison):
    def work(self):
        return "I come to the office and start to coding."

    def __str__(self):
        name_class = str(self.__class__)
        return f"{name_class[17:-2]}:{self.name}"


class Recruiter (Employee, Salary_comparison):
    def work(self):
        return "I come to the office and start to hiring."

    def __str__(self):
        name_class = str(self.__class__)
        return f"{name_class[17:-2]}:{self.name}"


michael = Developer("Michael", 1500)
print(michael)

emma = Recruiter("Emma", 1000)
print(emma)


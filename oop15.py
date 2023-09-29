class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def work(self):
        return "I come to the office."

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
        return f"{self.__class__}:{self.name}"


class Recruiter (Employee, Salary_comparison):
    def work(self):
        return "I come to the office and start to hiring."

    def __str__(self):
        return f"{self.__class__}:{self.name}"


michael = Developer("Michael", 1500)
print(michael)

emma = Recruiter("Emma", 1000)
print(emma)

print(michael.salary < emma.salary)
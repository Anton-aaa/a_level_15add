class Employee:
    email = ""
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return "I come to the office."

    def check_salary(self, days):
        return self.salary * days

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __le__(self, other):
        return self.salary <= other.salary


class Developer(Employee):
    def __init__(self, name, salary, tech_stack):
        super().__init__(name, salary)
        self.tech_stack = tech_stack

    def work(self):
        return "I come to the office and start to coding."

    def __str__(self):
        return self.__class__.__name__

    def __add__(self, other):
        return Developer(
            self.name + " " + other.name,
            set(self.tech_stack + other.tech_stack),
            max(self.salary, other.salary)
        )


class Recruiter(Employee):
    def work(self):
        return "I come to the office and start to hiring."

    def __str__(self):
        return self.__class__.__name__


michael = Developer("Michael",1500, ("Java", "JS", "C++"))
print(michael)
print("Salary calculation Michael in 10 days =", michael.check_salary(10))
print("Michael tech stack:", michael.tech_stack)

alisa = Developer("Alisa", 2000, ("PHP", "Java"))
print("Salary Alisa less salary Michael:", alisa.salary < michael.salary)
print("Quantity tech stack Alisa less tech stack Michael:",
      len(alisa.tech_stack) < len(michael.tech_stack))

emma = Recruiter("Emma", 1000)
print(emma)
print("Salary calculation Emma in 10 days =", emma.check_salary(10))

developer_sum = michael + alisa
print(
    developer_sum.name,
    developer_sum.salary,
    developer_sum.tech_stack
)



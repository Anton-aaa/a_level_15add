class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return "I come to the office."

    def check_salary(self, days):
        return (self.salary * days)

    def __gt__(self, other):
        return (self > other)

    def __lt__(self, other):
        return (self < other)

    def __ge__(self, other):
        return (self >= other)

    def __le__(self, other):
        return (self <= other)


class Developer(Employee):
    def __init__(self, name, salary, *tech_stack):
        self.tech_stack = tuple(tech_stack)
        super().__init__(name, salary)

    def work(self):
        return "I come to the office and start to coding."

    def __str__(self):
        name_class = str(self.__class__)
        return f"{name_class[17:-2]}:{self.name}"

class Create(Developer):
    def __new__(cls, obj_1, obj_2, **kwargs):
        return super().__new__(cls)

    def __init__(self, obj_1, obj_2):
        self.name = str(obj_1.name + " " + obj_2.name)
        self.tech_stack = set(obj_1.tech_stack + obj_2.tech_stack)
        if obj_1.salary <= obj_2.salary:
            self.salary = obj_2.salary
        else:
            self.salary = obj_1.salary


class Recruiter(Employee):
    def work(self):
        return "I come to the office and start to hiring."

    def __str__(self):
        name_class = str(self.__class__)
        return f"{name_class[17:-2]}:{self.name}"


michael = Developer("Michael",1500, "Java", "JS", "C++")
print(michael)
print("Salary calculation Michael in 10 days =", michael.check_salary(10))
print("Michael tech stack:", michael.tech_stack)

alisa = Developer("Alisa", 2000, "PHP", "Java")
print("Salary Alisa less salary Michael:", alisa.salary < michael.salary)
print("Quantity tech stack Alisa less tech stack Michael:", len(alisa.tech_stack) < len(michael.tech_stack))

emma = Recruiter("Emma", 1000)
print(emma)
print("Salary calculation Emma in 10 days =", emma.check_salary(10))

verification_create_object = Create( michael, alisa)
print("Name new object",verification_create_object.name)
print("Salary new object", verification_create_object.salary)
print("Tech stack new object", verification_create_object.tech_stack)

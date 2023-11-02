import csv
import traceback
from datetime import datetime


class Writer:
    def write(self, text):
        with open ("some_text.txt", "a") as f:
            f.write(f"{text}\n")

class Loger:
    def write(self, obj):
        number = 1
        with open("some_text.txt", "r") as f:
            for line in f:
                number += 1
        now = datetime.now()
        final = f"{number} {now.strftime('%d/%m/%Y %H:%M:%S')} {obj}"
        writer = Writer()
        writer.write(final)

def loger_decorator(function):
    def write_error(self):
        return function(self)

    error_register = Loger()
    error_register.write(write_error)
    return write_error






class EmailAlreadyExistsException(Exception):
    pass


class Employee:
    def __init__(self, name, salary, email):
        self.name = name
        self.salary = salary
        self.email = email

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


    @loger_decorator
    def save_email(self):
        try:
            self.validate()
            with open("emails.csv", "a") as f:
                f.write(f"{self.email} \n")
        except EmailAlreadyExistsException as e:

            print("ERROR. The email is already recorded in the file")
            return traceback.format_exc()


    def validate(self):
        with open("emails.csv") as f:
            for line in f:
                if self.email in line:
                    raise EmailAlreadyExistsException


class Developer(Employee):
    def __init__(self, name, salary, email, tech_stack):
        super().__init__(name, salary, email)
        self.tech_stack = tech_stack

    def work(self):
        return "I come to the office and start to coding."

    def __str__(self):
        return self.__class__.__name__

    def __add__(self, other):
        stack1 = set(self.tech_stack)
        stack2 = set(other.tech_stack)
        return Developer(
            self.name + " " + other.name,
            max(self.salary, other.salary),
            self.email + other.email,
            str(stack1 | stack2),
        )


class Recruiter(Employee):
    def work(self):
        return "I come to the office and start to hiring."

    def __str__(self):
        return self.__class__.__name__


class Candidate:
    def __init__(self,
                 first_name,
                 last_name,
                 email,
                 tech_stack,
                 main_skill,
                 main_skill_grade
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    def __str__(self):
        return self.main_skill_grade

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    @classmethod
    def generate_candidates(cls, file_location):
        candidates = []
        with open(file_location) as f:
            for index, line in enumerate(f):
                if index == 0:
                    continue
                incision = line.split(";")
                incision_name = incision[0].split() + incision[1:]
                candidates.append(Candidate(*incision_name))
            return candidates



if __name__ == "__main__":
    michael = Developer("Michael", 1500, "1", ("Java", "JS", "C++"))
    michael.save_email()
    print(michael)
    print("Salary calculation Michael in 10 days =", michael.check_salary(10))
    print("Michael tech stack:", michael.tech_stack)

    alisa = Developer("Alisa", 2000, "gmail", ("PHP", "Java"))
    alisa.save_email()
    print("Salary Alisa less salary Michael:", alisa.salary < michael.salary)
    print("Quantity tech stack Alisa less tech stack Michael:",
          len(alisa.tech_stack) < len(michael.tech_stack))

    emma = Recruiter("Emma", 1000, "ukrmail")
    print(emma)
    print("Salary calculation Emma in 10 days =", emma.check_salary(10))

    developer_sum = michael + alisa
    print(
        developer_sum.name,
        developer_sum.salary,
        developer_sum.tech_stack,
        developer_sum.email
    )

    corni_grant = Candidate("Corni",
                            "Grant",
                            "corni@gmeil.com",
                            ("Go", "Lisp", "Java"),
                            "Java",
                            "Senior"
                            )
    print(corni_grant.full_name)

    candidates = Candidate.generate_candidates("candidates.csv")



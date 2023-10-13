import csv

class EmailAlreadyExistsException(Exception):
    pass
class Employee:
    def __init__(self, name, salary, email):
        self.name = name
        self.salary = salary
        self.email = self.save_email(email)

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

    def save_email(self, email):
        try:
            self.validate(email)
            self.email = email
            with open("emails.csv", "a") as f:
                f.write(f"{email} \n")
        except EmailAlreadyExistsException:
            print("ERROR. The email is already recorded in the file")
        return email

    def validate (self, email):
        with open("emails.csv") as f:
            for line in f:
                if email in line:
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
        return Developer(
            self.name + " " + other.name,
            max(self.salary, other.salary),
            self.email + other.email,
            set(self.tech_stack + other.tech_stack),
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
    michael = Developer("Michael",1500,"1", ("Java", "JS", "C++"))
    print(michael)
    print("Salary calculation Michael in 10 days =", michael.check_salary(10))
    print("Michael tech stack:", michael.tech_stack)

    alisa = Developer("Alisa", 2000, "gmail", ("PHP", "Java"))
    print("Salary Alisa less salary Michael:", alisa.salary < michael.salary)
    print("Quantity tech stack Alisa less tech stack Michael:",
          len(alisa.tech_stack) < len(michael.tech_stack))

    emma = Recruiter("Emma",   1000, "ukrmail")
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
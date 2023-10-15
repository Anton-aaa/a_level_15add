from unittest import mock, TestCase
from program_code.oop15 import Employee, Developer, Recruiter, Candidate
from unittest.mock import Mock, patch

m = Mock()
class EmployeeTest(TestCase):
    def setUp(self):
        with patch.object("program_code.oop15.Employee.self.email", return_value=email):
            self.employee = Employee("Piter", 1000, "a")
            self.other_employee = Employee("Anri", 2000, "b")


    def test_work(self):
        self.assertEqual(self.employee.work(), "I come to the office.")

    def test_check_salary(self):
        self.assertEqual(self.employee.check_salary(10), 10000)

    def test_gt(self):
        self.assertFalse(self.employee.__gt__(self.other_employee))

    def test_lt(self):
        self.assertTrue(self.employee.__lt__(self.other_employee))

    def test_ge(self):
        self.assertFalse(self.employee.__ge__(self.other_employee))

    def test_le(self):
        self.assertTrue(self.employee.__le__(self.other_employee))

class DeveloperTest(TestCase):
    @patch('program_code.oop15.Employee.save_email', return_value="email")
    def setUp(self, mock_class):
        self.developer = Developer("Name", 1000, "email", "techStack")
        self.other_developer = Developer("Lesi", 1500, "email_2", "Java")

    def test_work(self):
        self.assertEqual(self.developer.work(), "I come to the office and start to coding.")

    def test_str(self):
        self.assertEqual(self.developer.__str__(), "Developer")

    @patch('program_code.oop15.Employee.save_email', return_value="email")
    def test_add(self, mock_class):
        self.assertEqual(self.other_developer.__add__(self.developer),
            Developer(self.other_developer.name + " " + self.developer.name,
            max(self.other_developer.salary, self.developer.salary),
            self.other_developer.email + self.developer.email,
            set(self.other_developer.tech_stack + self.developer.tech_stack)))


class RecruiterTest(TestCase):
    @patch('program_code.oop15.Employee.save_email', return_value="email")
    def setUp(self, mock_class):
        self.recruiter = Recruiter("Name", 1000, "c")

    def test_work(self):
        self.assertEqual(self.recruiter.work(), "I come to the office and start to hiring.")


class CandidateTest(TestCase):
    def setUp(self):
        self.candidate = Candidate(
            "First name",
            "Last name",
            "email",
            "tech stack",
            "main skill",
            "main skill grade"
        )

    def test_str(self):
        self.assertEqual(self.candidate.__str__(), "main skill grade")

    def test_full_name(self):
        self.assertEqual(self.candidate.full_name, self.candidate.first_name + " " + self.candidate.last_name)


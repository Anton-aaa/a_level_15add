from unittest import TestCase
from program_code.oop15 import Employee
from unittest.mock import Mock


class DeveloperTest(TestCase):
    def setUp(self):
        self.employee = Employee("2", "v", "a")

    def test_work (self):
        self.assertEqual(self.employee.work(), "I come to the office.")




#Abstraction question
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calc_salary(self):
        pass

class Intern(Employee):
    def calc_salary(self):
        return "intern salary is 12000"


class FullTimeEmployee(Employee):
    def calc_salary(self):
        return "FullTimeEmployee salary is 24000"

class ContractEmployee(Employee):
    def calc_salary(self):
        return "ContractEmployee salary is 36000"

E1=Intern()
print(E1.calc_salary())

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class Manager:
    def __init__(self,name,salary,team_size):
        super().__init__(name,salary)
        self.team_size=team_size
        

class Developer:
      def __init__(self,name,salary,programming_language):
        super().__init__(name,salary)
        self.programming_language=programming_language


manager1 = Manager("Rahul", 60000, 10)
developer1 = Developer("Aman", 50000, "Python")

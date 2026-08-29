class Person:

    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)


p1 = Person("Deepak")
p2 = Person("Deepak", 21)
p3 = Person("Deepak", 21, "Delhi")


p1.display()

p2.display()

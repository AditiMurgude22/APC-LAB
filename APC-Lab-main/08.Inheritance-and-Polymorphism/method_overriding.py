class Parent:
    def display(self):
        print("Parent method")

class Child(Parent):
    def display(self):
        print("Child method")

obj = Child()
obj.display()
class Parent:
    def display(self):
        print("Parent class")

class Child(Parent):
    def display(self):
        super().display()
        print("Child class")

obj = Child()
obj.display()
class Parent:
    def display(self):
        print("This is parent class")

class Child(Parent):
    def show(self):
        print("This is child class")

obj = Child()
obj.display()
obj.show()
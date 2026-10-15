class Father:
    def father(self):
        print("Father class")

class Mother:
    def mother(self):
        print("Mother class")

class Child(Father, Mother):
    def display(self):
        print("Child class")

obj = Child()
obj.father()
obj.mother()
obj.display()
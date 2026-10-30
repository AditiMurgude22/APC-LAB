class Student:

    def __init__(self):
        self.__name = "Rahul"
        self.__marks = 85

    def display(self):
        print("Name:", self.__name)
        print("Marks:", self.__marks)


s1 = Student()
s1.display()
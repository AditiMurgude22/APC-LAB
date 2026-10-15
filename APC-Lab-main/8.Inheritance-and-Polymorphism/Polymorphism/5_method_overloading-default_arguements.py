class Calculator:

    def add(self, a, b=0, c=0):
        return a + b + c


obj = Calculator()

print(obj.add(10))
print(obj.add(10, 20))
print(obj.add(10, 20, 30))
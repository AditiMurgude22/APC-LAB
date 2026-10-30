class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


def animal_sound(animal):
    animal.sound()


d = Dog()
c = Cat()

animal_sound(d)
animal_sound(c)
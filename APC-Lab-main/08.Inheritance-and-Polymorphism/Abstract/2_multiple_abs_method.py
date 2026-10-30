from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car starts with key")

    def stop(self):
        print("Car stops using brake")


obj = Car()
obj.start()
obj.stop()
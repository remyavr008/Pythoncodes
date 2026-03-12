from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def eat(self):
        print("animal eats")

class Cat(Animal): #we cant create object for abstarct class
    def sound(self):
        print("cat eats")
cat1=Cat()
cat1.sound()
cat1.eat()
from abc import ABC, abstractmethod

class Animal(ABC): # Abstract class
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks")

obj = Dog()
obj.sound()
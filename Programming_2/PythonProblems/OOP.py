"""We have previously looked at two paradigms of programming - imperative (using statements, loops, and functions as subroutines), and functional (using pure functions, higher-order functions, and recursion).

Classes are created using the keyword class and an indented block, which contains class methods (which are functions).
Below is an example of a simple class and its objects."""


class Cat:
    # __init__ is called when a instance of a class
    # is created. All __init__ must have a self because
    # when called, self is the name of th object.
    # self.attribute is how you access the attributes of an object.

    def __init__(self, color, legs):
        self.color = color
        self.legs = legs


felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)


"""Classes


The provided code defines a Student class, creates a Student object, and calls its greet() method.
However, the code has an error and does not run.
Fix the code to produce the expected output."""


class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(self.name+" says hi")


obj = Student("John")
obj.greet()


"""Inheritance"""


class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Cat(Animal):
    def purr(self):
        print("Purr...")


class Dog(Animal):
    def bark(self):
        print("Woof!")


fido = Dog("Fido", "brown")
tom = Cat("Tom", "black")
print(fido.color)
fido.bark()
tom.purr()


"""Inheritance


Complete the provided code to inherit the Car class from the Vehicle class, create a Car object and call its horn() method, which is inherited from the Vehicle superclass.
class Vehicle: 
  def horn(self):
    print("Beep!")

class Car:
  def __init__(self, name, color):
    self.name = name
    self.color = color

obj = Car("BMW", "red") """


class Vehicle:
    def horn(self):
        print("Beep!")


class Car(Vehicle):
    def __init__(self, name, color):
        self.name = name
        self.color = color


obj = Car("BMW", "red")
obj.horn()


""""""

# Object oriented programming
# way of organising code around objects

# an object represents real-world entity that has
# attributes > data/properties > store data about an object
# methods > behaviour/actions > functions defined inside a class

class Student:
    pass

student1 = Student()

# classes > is a blueprint
# an object is an instance created from that blueprint

class Student:
    def introduce(self):
        print("Hello , I am a student")


# student1 = Student()
# student1.introduce()


class Student :

    # init is a special method that runs automatically when an object is created. 
    # def __init__(self,name,age):
    #     self.name = name
    #     self.age = age

    def introduce(self):
        print(f"hello i am a {self.name} and i m {self.age} years old")

    def set_name(self,name):
        self.name = name
        


# student1 = Student("Reema",24)
# student1.introduce()

# self > refers to the current object, used to access attributes and methods inside the class, outside the class it doesn't make any sense

student1 = Student()
student1.set_name("Reema") # > Student.set_name("student1","Riya")
print(student1.name)


# instance  attributes vs class attributes

# IA >  belongs to individual objects
# CA > shared by all the objects of a class

class Student:
    school = "algocamp"

    def __init__(self,name):
        self.name = name
    

student1 = Student("Reema")
student2 = Student("yachna")

print(student1.name)
print(student2.name)
print(student1.school)
print(student2.school)


# method overriding : a child class provides its own version of a method already defined in parent class

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal) :
    def sound(self):
        print("Dog sounds")


dog = Dog()
dog.sound()


# super is basically used to call methods of parent class

class Person:
    def __init__(self,name):
        self.name = name

class Student(Person):
    def __init__(self, name,course):
        super().__init__(name)
        self.course = course

    def __str__(self):  #how this object will be printed 
        return f"Student name is {self.name}"
    

student1 = Student("Reema","Python")
print(student1)
print(student1.name)
print(student1.course)


# Encapsulation : 

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance  # _balance means intended for internal use, doesn't make it truly private but tells other developer not to use it
    

# name = public , _name : protected, __name : name mangling (harder to use outside)


# dunder / magic methods

# special methods that starts and ends with double underscore

# __init__ , __str__ , __len__ , __eq__ , __add__



class Course:
    def __init__(self,students):
        self.students = students

    def __len__(self):
        return len(self.students)
    

course = Course(["Reema","yachna","yashika"])

print(len(course))


class Student:
    def __init__(self,marks):
        self._marks = marks

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self,value):
        if value < 0:
            raise ValueError("marks cannot be negative")
        self._marks = value

    
student1 = Student(90)

print(student1.marks)

student1.marks = 96

print(student1.marks)

# property is getter
# marks.setter is setter


# class methods

class Student:
    school="algocamp"

    def __init__(self,name):
        self._name = name

    @classmethod
    def change_school(cls,new_school):
        cls.school = new_school


Student.change_school("dps")

print(Student.school)


# static methods : belongs to a class , do not use self, cls. they are utility method inside a class for logical grouping

class MathUtils:
    @staticmethod
    def add(a,b):
        return a + b
    

print(MathUtils.add(10,20))


# diff between class methods vs static methods

# Dataclasses > helps us to create classes mainly used for storing data

# they reduce boilerplate code like writting __init__ manually.

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    course: str


student1 = Student("reema",24,"python")
print(student1)

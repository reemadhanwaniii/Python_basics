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

student1 = Student("Reema","Python")
print(student1.name)
print(student1.course)
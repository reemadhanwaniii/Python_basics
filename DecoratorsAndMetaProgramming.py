# First class functions : functions are first class objects

def greet() :
    return "hello"


message = greet
print(message())


def shout(text) :
    return text.upper()

def process(func,value):
    return func(value)

print(process(shout,"python"))


def outer() :
    def inner() :
        print("Inside inner function")

    return inner

func = outer()

func()


# decorators : a function that takes another function,add extra behaviour and returns a new function


def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")

    return wrapper


def say_hello():
    print("hello")

decorator_funct = my_decorator(say_hello)
decorator_funct()


@my_decorator
def say_hi():
    print("hii")

say_hi()



def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args,**kwargs)
        print("After function call")
        return result

    return wrapper


@my_decorator
def add(a,b):
    return a+b

print(add(78,8))


# logging decorator

def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Before function call: {func.__name__}")
        result = func(*args,**kwargs)
        print(f"After function call: {func.__name__}")
        return result

    return wrapper


@log_function
def add(a,b):
    return a+b

print(add(78,8))


# timing decorator

import time


def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()

        print(f"{func.__name__} took {end-start} second")
        return result

    return wrapper


@timer
def slow_function():
    time.sleep(2)
    print("done")

slow_function()


# functools.wraps

# when we use decorators the original function name and docstring can actually be replaced by the wrapper function details as well



def my_decorator(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)

    return wrapper

@my_decorator
def say_hello():
    """This function greets the user."""
    print("hello")


print(say_hello.__name__)
print(say_hello.__doc__)


from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)

    return wrapper

@my_decorator
def say_hello():
    """This function greets the user."""
    print("hello")


print(say_hello.__name__)
print(say_hello.__doc__)


# class decorators
# a function that takes a class, modifies it and returns it


def add_greeting(cls):
    cls.greet = lambda self: "Hello from decorated class"
    return cls


@add_greeting
class Student:
    def __init__(self,name):
        self.name = name

student = Student("Reema")

print(student.name)
print(student.greet())


# Introspection > means inspecting objects at runtime
# python allows us to check what attributes and methods an object has


class Student:
    school = "algocamp"

    def __init__(self,name):
        self.name = name

    def introduce(self):
        print("My name is {self.name}")


student = Student("Reema")

print(dir(student))
print(getattr(student,"name"))
print(getattr(student,"age","Age not found"))
setattr(student,"age",24)
print(student.age)
print(hasattr(student,"marks"))
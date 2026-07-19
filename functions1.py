def greet():
    print("hey , hello")

greet()

def subtract(a,b):
    res = a-b
    print(res)
    return res


subtract(3,4)


# keyword arguments passed using parameter names, so the order doesn't matter

def introduce(name,age):
    print(f"my name is {name} and age is {age}")

introduce(age=24,name="reema")


# default arguments

def greet(name="Student"):
    print(f"Hello ,{name}")


greet();
greet("reema")

# args allows function to accept any number of positional arguments, it stores them as a tuple

def add_numbers(*args):
    return sum(args)

print(add_numbers(1,3,6))
print(add_numbers(3,6))

# kwargs allows a function to accept any number of keyword argumnets ,it stores them as a dictionary

def show_profile(**kwargs):
    print(kwargs)

show_profile(name="reema",age=24,gender="F")


def square(n):
    return n*n

print(square(6))


def calculate(a,b):
    return a+b,a-b,a*b,a/b


add,subtract_,multiply,division = calculate(78,7)

print(add,subtract_,multiply,division)


# Scope
# a variable created inside a function is local and can only be used inside that function

def greet():
    message="hello"
    print(message)


# print(message) error

# global > a variable created outside all functions is global and can be accessed inside function 

name = "Reema"

def demo():
    print(name)

demo()

# global keyword is used when we want to modify a global variable inside a function

count = 0
def increment():
    global count # means i wnat to modify global count variable
    count += 1
    print(count)

increment()


# nonlocal keyword is used in nested functions to modify a variable from outer function


def outer():
    count = 0
    def inner():
        nonlocal count
        count+=1
        print(count)
    inner()

outer()


#lambda expressions are basically small anonymous functions used for short term operations


square = lambda x:x*x
print(square(5))

is_even = lambda num: num%2==0
print(is_even(7))


# DocStrings used to describe what a function does. they are usually written inside triple quotes

def add(a,b):
    """
    Adds to numbers and return result
    """
    return a+b

print(add(4,5))


# type annotations describe the expected input and output types of a function

def add(a:int, b:int) -> int:
    return a+b

# print(add(7,"reema")) error

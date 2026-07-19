# function is basically a block of code to perform specific task
# functions are basically of 2 types :
#  standard library functions, user-defined functions


def greet():
    print("hello world")

greet()

def add_numbers(a,b):
    print("sum is : ",a+b)


add_numbers(4,5)

# error
# def add_number(a,b):
#     print("sum is : "a+b)

# add_number(8,7)

# functions with return types

def find_square(num):
    square = num*num
    return square


result = find_square(7)
print(result)


print(pow(2,3)) # predefined function
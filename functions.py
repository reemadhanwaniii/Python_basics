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



# python list
# used to store multiple data at once

number = [1,2,4,6]
print(number)

my_list = [1,"hello",3.15]
print(my_list)


my_list.append("78")
print(my_list)


prime_number = [2,3,5]
even_number =[4,6,8]
odd_number = [1,3,5]

prime_number.extend(even_number)
print(prime_number)

my_list[1] = 54
print(my_list)

# delete something from list
del my_list[1]
print(my_list)

my_list.remove("78")
print(my_list)

print(3.14 in my_list)
print(3.15 in my_list)


print(len(my_list))
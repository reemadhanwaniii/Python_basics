print("hello world");

# python identifiers
language = "python"

# keywords 
# continue = "hello" 

# rules for naming identifiers

# identifiers cannot be keyword
# identifiers are case sensitive score and Score are different variables
# It can hava a sequence of letter and digits, however it must always begin with letter or _, the first letter of an identifier cannot be a digit
# Its usually a convention to start an identifier with a letter rather than _
# whitespaces are not allowed
# we cannot use special characters like @, #


print(language);

add_  = 10+67
print(add_)

language = "java"
print(language)

a,b,c = 3,4.6,"hello"

print(a);
print(b)
print(c)

site1 = site2 = "programize.com"
print(site1)
print(site2)

# constant
PI = 3.14 
print(PI)

result = True
print(result)


# Pyhton Datatypes

# Data types specify the type of data that can be stored inside a variable
num = 24 

# numeric - integer,floating
# String
# sequence - list, tuples,range
# Mapping -> dict
# Boolean -> bool
# Set -> set,frozenset


num1 = 5
print(type(num1))

# Everything is an object in python programming datatypes are classes and variables  are instance of this classes
num2 = 5.4
print(type(num2))


# python list data type
# list is an ordered collection of similar or different types of items seperated by commas and enclosed within brackets [].

language = ["java","C++","python"]

print(language)
print(language[0])


# python tuple data types

# tuples is an ordered sequence of items same as list . The only difference is that tuples are not immutables.Tuples once created cannot be modified
product = ('Xbox',1000)
print(product[0])
print(product[1])


# python string data type
# string is a sequence of characters represented by either single or double quotes

name = "Python"
print(name)

message = 'python is programming language'
print(message)

#  python set data type
# set is an unordered collection of unique elements ,set is defined by values seperated by comma inside braces {}

student_id = {1,2,3,4,5}
# indexing is not applied here
print(student_id)

print(type(student_id))

# python dictionary data type
# dictionary is an ordered collection of items, it stores elements in key/value pairs
# keys are unique identifiers that are associated with each value .

capitals = {'Nepal' : 'Kathmandu','Italy' : 'Rome'}

print(capitals)

print(capitals['Nepal'])


# Type conversions is basically process of converting one type to another

# Implicit -> automatic type conversion
# explicit -> manual type conversion

# Implicit

integer = 124
floatnumber = 1.23

val = integer + floatnumber
print(val)
print(type(val))

# python always convert smaller to larger data type to avoid loss of data  

# Explicit

num_string = '12'
num_integer = 12

print(type(num_string))
num_string = int(num_string)
print(type(num_string))


num_sum = num_string + num_integer
print(num_sum)

# python input and output

print("python is "+" awesome")
x = 5
y = 10

print('the value of x is {} and the value of y is {}'.format(x,y))


# python input
# input(prompt)

num = input('Enter a number : ')

# arithmetical operators +,-,*,/,%,**

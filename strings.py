# Strings
# string is a sequence of characters used to store text


name = "Algocamp"
message = "python is fun"


# strings are immutable meaning they cannot be changed directly after creation
s1 = "hello"
s2 = 'hello'
s3 = """hello"""


sentence = "i'm learning python"
quote = 'he said ,"python is easy"'

text = "python"


# strings are indexed from 0
print(text[0])
print(text[-1])

# slicing
print(text[0:3])
print(text[:4])
print(text[2:])
print(text[::-1])

# slicing doesn't modify the original string.

# methods

name = "python programming"
print(name.upper());
print(name.capitalize());
print(name.title());

text = "I love Python"

print(text.find('Python'))
print("Python" in text)

email = "          test@gmail.com           "
print(email)
print(email.strip())


sentence = "python is useful"
words = sentence.split()
print(words)

joined = "-".join(words)
print(joined)

text = "i like java"
print(text.replace("java","python"))

# string formatting
name = "Reema"
age = 24

print(f"My name is {name} and age is {age} years old")  # f strings are considered modern and readable

print("my name is {} and age is {}".format(name,age))
print("my name is %s and age is %d old" % (name, age))


message = """"hello
welcome to python strings
let's learn""" #multi-line strings

path = r"C:\users\reema\documents" #raw strings
print(path)

# escape sequences

print("hello\nworld")
print("she said \"Python is easy\"")

# \n > newline
# \t > tab
# \\ backslash
# \" double quote
# \' single quote

# python strings support unicode by default

text = "Hello "
print(ord("A"))
print(chr(65))

# python string > bytes using UTF-8 encoding
text = "python"  # normal string , type > str
encoded = text.encode("utf-8")
print(encoded) # output b'python > the b before the python means this is python object,not a normal string
# iteratable >  an iterable is any object that can be looped over using a for loop

numbers = [1,2,3]

name="python"
student={"name":"reema","age":23}

# for item in numbers:
#     print(item)

# for item in name:
#     print(item)

# for item in student:
#     print(item)


# list,tuple,string,dictionary,set,range, file object

# iterables vs iterators
# iterator is the actual object that gives values one by one


numbers = [10,20,30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))


# iterator protocol : an object should have __iter__  > return iterator object itself and __next__  return the next value

numbers = [10,20,20]

iterator = iter(numbers)

print(iterator.__next__())

# stopIteration

# generators > are simple way to create iterators


# __iter__ , __next() instead of writing this we use function yield


def count_up_to(limit):
    current = 1
    while current <= limit:
        yield current  #pause a function and returns value , when generator is called again it continues from where it was paused
        current+=1


for num in count_up_to(3):
    print(num)


def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()

print(next(gen))
print(next(gen))
print(next(gen))


# generators are memory efficient because they produce value one at a time


numbers = [x*x for x in range(10000000)]

# iterators will create this full list in memory in one go
#  generators will not create full list in one go, it give one value at a time


# generators expressions

square = [x*x for x in range(5)]

print(square)


square = (x*x for x in range(5))
print(square)
print(next(square))
print(next(square))
print(next(square))


# map() > applies a function to every item in an iterable

numbers = [1,2,3,4]

squares = map(lambda x: x*x,numbers)
print(list(squares))

def square(x):
    return x*x

numbers = [1,2,3,4,5]

square = map(square,numbers)
# print(next(square))
# print(next(square))
# print(next(square))
# print(next(square))


# filter() keeps only the items that match the condition

numbers = [1,2,3,4,5,6]

even_numbers = filter(lambda x: x%2==0,numbers)
print(list(even_numbers))

# reduce() > available in functools module

from functools import reduce

num = [1,2,3,4,5,6]

product = reduce(lambda a,b: a*b,numbers)
print(product)

# function programming means writing code using functions as main building block

# function can be:
# stored in a variable
# passed as arguments
# retured from other functions
# can be used inside data transformation


def sq(x):
    return x*x


operation = sq
print(operation(5))


# higher order function > that expects other function as a argument or it return function

def apply_operation(func,value):
    return func(value)


def sq(x):
    print(x*x)

apply_operation(sq,5)


# closures > when inner function remember variables from the outer function even after the outer function is finished

def multiplier(factor):
    def multiply(number):
        return number*factor
    
    return multiply

double = multiplier(3)
print(double(7))


# functools > provide tools for working with functions

# reduce, partial, lru_cache, wraps


# functools.partial > partial() lets us create a new function by fixing some arguments of an existing functions


from functools import partial

def power(base,exponent):
    return base**exponent


square = partial(power,exponent=2)
cube = partial(power,exponent=3)


print(square(5))
print(cube(5))


# itertools > provide efficient tools for working with iterators

# chain > combines multiple iterables into one sequence


from itertools import chain

list1 = [1,2,4,5]
list2 = [6,7,8,9]

combined = chain(list1,list2)

print(list(combined))

# combinations > basically gives possible selection using repeating order

from itertools import combinations

items = ["A","B","C"]

result = combinations(items,2)

print(list(result))

# permutation
# type hints > allows us to mention the expected type of variables , function parameter and the return value as well
# python is dynamically types , so type hints do not enforce types at runtime by default


def greet(name: str) -> str:
    return f"hello {name}"

print(greet(10))
print(greet("reema"))


age : int = 10
age1 : int = "reema"

print(age)
print(age1)


def add(a: int,b: int) -> int:
    return a + b


result = add(10,20)

print(result)


def print_mesage(message: str) -> None:
    print(message)


# the typing module provides many useful types for writting better type hints


from typing import Optional, Union, Any, TypedDict, NamedTuple

# generics allows us to mention what type of data a collection contains

numbers: list[int] = [1,2,3,4]
name: list[str] = ["reema","yachna"]

def total(numbers: list[int]) -> int:
    return sum(numbers)


print(total([10,20,30]))


# generics : dict[k,v]

student: dict[str,int] = {
    "math": 90,
    "english": 67,
    "hindi": 78
}


def print_scores(scores: dict[str,int]) -> None:
    for subject,marks in scores.items():
        print(subject, marks)


print(print_scores(student))


coordinates: tuple[int, int] = (10,20)
unique_numbers: set[int] = {1,2,8}


# Optional is used when a value can either be of a specific type or none

from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "reema"
    return None

def find_user(user_id: int) -> str | None:
    if user_id == 1:
        return "reema"
    return None


# Union is used when a value can be  one of multiple types

from typing import Union

def format_id(user_id : Union[int, str]) -> str:
    return f"User-{user_id}"

def format_id(user_id : int | str) -> str:
    return f"User-{user_id}"


# any means the value can be of any type

from typing import Any

def print_value(value :Any) -> None:
    print(value)

# typeDict used to define the expected structure of a dictionary


from typing import TypedDict

class Student(TypedDict):
    name: str
    age: int
    course: str

student: Student = {
    "name": "Reema",
    "age": 24,
    "course": "python"
}


def print_student(student: Student) -> None:
    print(student["name"])
    print(student["course"])

print_student(student)


# protocol > is used to define expected behaviour instead of exact class inheritance

from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None:
        ''
    
class Circle:
    def draw(self) -> None:
        print("Drawing circle")

class Square:
    def draw(self) -> None:
        print("Drawing square")

    

def render(shape: Drawable) -> None:
    shape.draw()

render(Circle())
render(Square())


# static type checking > means checking type errors before running the program

def add(a:int,b:int) -> int:
    return a+b

add("10","20")

# mypy used for static type checking(read more about it)
# pyright

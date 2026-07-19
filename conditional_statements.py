# if
 

number = 10

if number > 0:
    print("number is positive")

print("if is executed")


number = -2

if number > 0:
    print("number is positive")
else:
    print("number is negative")

number = 0

if number > 0:
    print("number is positive")
elif number < 0:
    print("number is negative")
else:
    print("number is 0")


# nested if

number = 5

if number >= 0:
    if number == 0:
        print("number is 0")
    else:
        print("number is positive")
else:
    print("number is negative")
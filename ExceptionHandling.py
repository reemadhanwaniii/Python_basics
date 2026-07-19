# exceptions are errors that occur while the program is running.
#  if they are not handled , the program stops execution

# num = int('abc')


# value error
# fileNotFound error
# index error
# key errors
# type errors
# zerodivision errors


# traceback : a traceback basically shows  where the error happened and what type of error occured


# def divide(a,b):
#     return a/b


# divide(4,0)


# try and except

# try is used to write risky code, except basically handles  the error if something goes wrong


# try:
#     num = int(input("Enter a number : "))
#     print(num)
# except ValueError:
#     print("Enter valid value")
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except:
#     print("genric error")
# else:
#     print("conversion successful")
# finally: 
#     print("always executing")



# #  broad exception catches almost every error

# try:
#     result = 10/0
# except Exception:
#     print("something went wrong")


# try:
#     result = 10/0
# except Exception as e:
#     print("something went wrong", e)


# # manually raise exception 

# def withdraw(balance,amount) :
#     if amount > balance:
#         raise ValueError("Insufficient, balance")
    
#     return balance - amount


# print(withdraw(1000,150000))


# Custom exception helps us to create meaningful errors for our own application


# class InSufficientBalanceError(Exception):
#     pass

# def withdraw(balance,amount):
#     if amount > balance:
#         raise InSufficientBalanceError("Not enough balance")

#     return balance - amount

# try:
#     withdraw(100,1500)
# except InSufficientBalanceError as e:
#     print(e)    




# # Exception chaining happens when one exception happens becaue of another exception

# def convert_to_int(value):
#     try:
#         return int(value)
#     except ValueError as e:
#         raise ValueError("Failed to convert value to integer") from e
    

# convert_to_int("abc")


# finally > cleanup

file = None

try:
    file = open("data.txt","r")
    content = file.read()
except:
    print("file not found")
finally:
    if file:
        file.close()
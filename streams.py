# standard streams > python has three standard streams that handle input, output and errors

# stdin > standard input
# stdout > standard output
# stderr > standard error


# standard input
name = input("Enter your name : ")
print(name)


# import sys

# data = sys.stdin.readlines()

# print(data)


# stdout

print("normal output")

import sys

sys.stdout.write("hello from stdout")


# stderr
sys.stderr.write("hello from stderr")

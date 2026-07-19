# r = read
# w = write
# a = append
# x = create a new file , fails if file exists
# rb = read binary
# wb = write binary


file = open("image.png","rb")
data = file.read();
file.close()


file = open("notes.txt","a")
file.write("\nHello python\n")
file.close()

# # context manager 
# # with statement automatically closes after the file use

with open("notes.txt","r",encoding="utf-8") as file:
    content = file.read()

print(content)


with open("notes.txt","w",encoding="utf-8") as file:
    file.write("Learning File I/O in python")


# os.path > helps us work with file and folder paths

import os

path = "notes.txt"

print(os.path.exists(path))
print(os.path.abspath(path))


file_path = os.path.join("data","notes.txt")
print(file_path)

# pathlib > modern and cleaner way to work with file paths in python
# it treats path like objects so the code becomes easier to understand


from pathlib import Path

path = Path("notes.txt")

print(path.exists())
print(path.absolute())


content = path.read_text(encoding="utf-8")

print(content)

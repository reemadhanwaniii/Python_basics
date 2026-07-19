# for loop

languages = ["java","python","c++","C#","javascript"]

for language in languages:
    print(language)



# range function

values = range(4)
for i in values:
    print(i)


# while loop

i=1
n=5

while(i <= n):
    print(i);
    i+=1



for i in range(4):
    print(i)

# python doesn't give in-built do-while loop

# break and continue

for i in range(5):
    if i==3:
        break
    else:
        print(i)


for i in range(5):
    if i==3:
        continue
    else:
        print(i)


# switch statement
language = "javascript"

match language:
    case 'javascript':
        print("yes")
    case 'java':
        print("yes")
    case _:
        print("no")

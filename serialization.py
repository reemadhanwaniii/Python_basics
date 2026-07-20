# Serialization: converting python data into a format that can be saved in a file or transferred over a network


student = {
    "name" : "reema",
    "age" : 25
}


# json > readable text format
# csv > tabular data format
# pickle > python specific binary format


student = {
    "name" : "reema",
    "age" : 25
}


import json


student = {
    "name" : "reema",
    "age" : 25
}


with open("student.json","w",encoding="utf-8") as file:
    json.dump(student,file)



with open("student.json","r",encoding="utf-8") as file:
    data = json.load(file)

print(data)


# csv = comma seperated value, used to store data in tabular format
# excel, google sheets

# name,age
# reema,24
# yachana ,29


import csv

student = [
    ["name","age"],
    ["reema",24],
    ["yachna",29]
]

with open("student.csv","w",newline="",encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(student)


with open("student.csv","r",encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# Dictwriter is used when data is stored as dictionary


# pickel : used to stored python object as binary(dict ,list,tuple,set)

import pickle

student = {
    "name" : "Reema",
    "age" : 24
}

with open("student.pkl","wb") as file:
    pickle.dump(student,file)


with open("student.pkl","rb") as file:
    data = pickle.load(file)

print(data)


# rb : read binary , load = load binary from pickle file


# do not load pickle file from unknown sources
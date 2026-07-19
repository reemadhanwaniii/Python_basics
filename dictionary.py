# collection of items, stores elements in key-value pairs , keys are unique identifiers associated with each value


capitals = {'Nepal' : 'kathmandu','Italy' : 'Rome','England' : 'Rome'}
print(capitals)

capitals['Japan'] = 'Tokyo'
print(capitals)

capitals['Italy'] = 'Florence'
print(capitals)

print(capitals['England'])


del capitals['Italy']
print(capitals)

map = {1:2,3:4}
print(map)

del map
print(map)

print('England' in capitals)

for i in capitals:
    print(i)
    print(capitals[i])


# set : elements of set cannot be duplicated 

student_id = {112,114,423,234,132}
print(student_id)

num = {1,1,2,2}

print(num)

num.update(student_id)
print(num)

num.discard(2);
print(num)

print(len(num))
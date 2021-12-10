import numpy as np

with open('input.txt') as f:
    lines = f.read()
lines = lines.strip("\n")
list2 = []
ints = 0

def Convert(string):
    list2=[]
    list2[:0]=string
    return list2

input = (Convert(lines))


for element in (input):
    list2.append(element.strip("\n"))


for i in range (0, 100):
    list2.insert(i, 9)

for i in range (11000, 11100):
    list2.append(9)

for i in range(100, (len(list2 - 100))):
        if list2[i] < list2[i+100] and list2[i] < list2[i-100] and list2[i] < list2[i-1] and list2[i] < list2[i+1]:
            ints = ints + ((int(list2[i])) + 1)
#     except:
#         pass
print(ints)


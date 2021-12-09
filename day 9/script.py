with open('input.txt') as f:
    lines = f.read()

lines = lines.strip("\n")


def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

input = (Convert(lines))

integers = 0
print(input)
print(len(input))

for i in range(len(input)):
    try:
        if:
        if input[i] < input[i+100] and input[i] < input[i-100] and input[i] < input[i-1] and input[i] < input[i+1]:

            integers = integers + (int(input[i]) + 1)
    except:
        pass
print(integers)

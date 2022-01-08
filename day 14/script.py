with open ("input.txt", "r") as myfile:
    data = myfile.read().splitlines()
    data.pop(1)

tracker = 0
element = data[0]
current = ""
temp = ""

def break_element(element):
    element_list = [element[i:i+2] for i in range(len(element))]
    return element_list

a = break_element(element)
print(a)


while tracker < 10:
    element_list = break_element(element)
    for line in data[1:]:
        current = str(line[0] + line[1])
        for i in enumerate(element_list):
            print(i)
            if i[1] == current:
                b = str(line[6])
                print(f"The current element is {current} and the next element is {b}")
                temp_char = i[1]
                temp_char = temp_char[0]
                temp_int = i[0]
                print(f"The temp variable is {temp_char} and the temp_int is {temp_int}")
                element = element[:temp_int] + b + element[temp_int:]

    tracker += 1

print(element)



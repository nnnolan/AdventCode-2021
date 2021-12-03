# advent calender day 2
horizontal_sum = 0
vertical_sum = 0



with open(r"C:\Users\Nolan\Documents\GitHub\AdventCode-2021\day 2\input.txt", "r") as text_file:
    for line in text_file:
        current_line = line.split() # makes list 

        print(current_line)
        if current_line[0] == 'forward': #forwards  movement
            horizontal_sum += int(current_line[1])

        elif current_line[0] == 'down': #down moemnt
            vertical_sum += int(current_line[1])

        elif current_line[0] =='up': #up movement
            vertical_sum -= int(current_line[1])


print(f"The sum of the horizontal changes is {horizontal_sum}")
print(f"The sum of the vertical changes is {vertical_sum}")
final = horizontal_sum * vertical_sum
print(f"The final answer is the product of horizontal and vertical sums, which is {final}")

print("-------------------------------------------")

file = open(r"C:\Users\Nolan\Documents\GitHub\AdventCode-2021\day 2\input.txt", "r")
data = file.read()


horizontal_sum = 0
vertical_sum = 0
aim = 0


for line in data:
    newLine = line.split()
    if newLine[0] == 'forward':
        horizontal_sum += int(newLine[1])
        vertical_sum += int(newLine[1]) * aim
    elif newLine[0] == 'down':
        aim += int(newLine[1])
    elif newLine[0] =='up':
        aim -= int(newLine[1])

print("Part 2")
print(f"The sum of the horizontal changes is {horizontal_sum}")
print(f"The sum of the vertical changes is {vertical_sum}")
final = horizontal_sum * vertical_sum
print(f"The final answer is the product of horizontal and vertical sums, which is {final}")
print("-------------------------------------------")
# advent calender day 1 
with open(r"C:\Users\Nolan\Documents\GitHub\AdventCode-2021\day 1\input.txt", "r") as f:
    input_values = [int(n) for n in f.read().splitlines()]

count = 0

for i, _ in enumerate(input_values): # checks each value in the list
    if input_values[i] > input_values[i-1]:
        count += 1

print(f"The data increased {count} many times :*)") # woo hoo
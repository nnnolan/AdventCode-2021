with open("input.txt") as fh:
    lines = fh.readlines()

# read in the height map
hmap = [[int(y) for y in x.strip()] for x in lines]

# add 9's around the edges of the height map; simplifies further processing

for i in range(len(hmap)):
    hmap[i].append(9)
    hmap[i].insert(0, 9)

# add 9-rows to the top and bottom of the height map
nines = [9] * (len(hmap[0]))
hmap.append(nines)
hmap.insert(0, nines)

risksum = 0
for row in range(1, len(hmap)-1):
    for col in range(1, len(hmap[0])-1):
        # find the local minima
        if hmap[row][col] < min([hmap[row+1][col],hmap[row-1][col],
                                 hmap[row][col+1],hmap[row][col-1]]):
            risksum += hmap[row][col] + 1 # risk = height + 1

print(f"Part 1: Sum of the risk levels: {risksum}")
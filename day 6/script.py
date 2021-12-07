fishes = [int(i) for i in open("input.txt","r").readline().split(',')] 
def age(days):
	fishes = 10*[0]
	for f in fishes:
		fishes[f] += 1
	for d in range(days):
		for i in range(len(fishes)):
			if i == 0:
				fishes[8+1] += fishes[0]
				fishes[6+1] += fishes[0]
				fishes[0] = 0
			else:
				fishes[i-1] = fishes[i]
				fishes[i] = 0
	return (sum(fishes))
print("Part1: %d" % age(80))
print("Part2: %d" % age(256))
from collections import Counter

ll = [x for x in open(r"C:\Users\Nolan\Documents\GitHub\AdventCode-2021\day 2\input.txt").read().strip().split('\n')]

theta = ''
epsilon = ''
for i in range(len(ll[0])):
	common = Counter([x[i] for x in ll])
	if common['0'] > common['1']:
		theta += '0'
		epsilon += '1'
	else:
		theta += '1'
		epsilon += '0'
print(int(theta,2)*int(epsilon,2))
from collections import Counter

def model_lf(days, data):
    for _ in range(days):
        data.append(data.pop(0))
        data[6] += data[-1]
    return sum(data)

with open("input.txt") as f:
    c = Counter(list(map(int, f.read().split(','))))
    data = [c[i] for i in range(9)]
    print(f"Part One: {model_lf(80, data[:])}") # 386536
    print(f"Part Two: {model_lf(256, data[:])}") # 1732821262171
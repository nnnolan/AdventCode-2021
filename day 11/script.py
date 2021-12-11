lines = [
    [4, 8, 3, 6, 4, 8, 4, 5 , 5, 5],
    [4, 6, 6, 3, 8, 4, 1, 7, 7, 2],
    [3, 5, 1, 2, 4, 8, 4, 5, 5, 6],
    [1, 4, 8, 1, 5, 4, 7, 5, 7, 2],
    [7, 7, 4, 1, 1, 8, 3, 4, 2, 2],
    [8, 6, 8, 3, 2, 2, 2, 8, 8, 2],
    [4, 2, 1, 5, 2, 4, 4, 2, 3, 3],
    [1, 5, 4, 4, 7, 1, 2, 1, 7, 1],
    [5, 7, 2, 5, 8, 5, 5, 7, 8, 6],
    [1, 7, 1, 7, 3, 8, 2, 2, 8, 1], 
]

days = 3
def findflashes(lines, days):
    repeat = 0
    while repeat != days:
        for line in lines:
            for i in line:

                if line[i] + 1 != 10:
                    line[i] += 1

                else:
                    line[i] = 0
                    if line[i+1] + 1 != 10:
                        line[i+1] += 1
                    else:
                        line[i+1] = 0
                        if line[i+2] + 1 != 10:
                            line[i+2] += 1
                        else:
                            line[i+2] = 0
        repeat += 1
    return lines


findflashes(lines, days)
a = findflashes(lines, days)
print(a)

# 4836484555
# 4663841772
# 3512484556
# 1481547572
# 7741183422
# 8683222882
# 4215244233
# 1544712171
# 5725855786
# 1717382281
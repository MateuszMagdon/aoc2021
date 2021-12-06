
input = list(map(lambda x: int(x), open("6/input.txt").read()[:-1].split(',')))

#input = [3,4,3,1,2]

for day in range(80):
    to_add = 0
    for index, el in enumerate(input):
        if el == 0:
            to_add += 1
            input[index] = 6
        else:
            input[index] = el-1
    input += [8] * to_add


print(len(input))

#1 = 353079
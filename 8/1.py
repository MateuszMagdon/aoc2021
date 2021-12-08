
lines = [line.split('|') for line in open("8/input.txt").read().strip().split('\n')]
outputs = [line[1].split() for line in lines]

sum = 0
for output in outputs:
    for digit in output:
        if len(digit) in [2, 4, 3, 7]:
            sum += 1

print(sum)
#534
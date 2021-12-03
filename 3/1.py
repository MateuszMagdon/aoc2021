


#gamma - most common bits
#epsilon - least common bits

calc = [0,0,0,0,0,0,0,0,0,0,0,0]

for line in open('3\input.txt'):
    for index, char in enumerate(line[:-1]):
        if char == '1':
            calc[index] += 1
        else:
            calc[index] -= 1

gamma = 0
for index, item in enumerate(calc[::-1]):
    if item > 0:
        gamma+=2**index

epsilon = 0
for index, item in enumerate(calc[::-1]):
    if item < 0:
        epsilon+=2**index

print(gamma * epsilon)

#4160394
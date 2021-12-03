
#gamma - most common bits
#epsilon - least common bits

gamma = epsilon = ''
tmp=0
for index in range(0,12):
    for line in open('3\input.txt'):
        if line[index] == '1':
            tmp += 1
        else:
            tmp -= 1

    if tmp > 0:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

    tmp = 0

print(int(gamma, 2) * int(epsilon, 2))

#4160394
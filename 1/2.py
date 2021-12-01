import os

ints = list(map(lambda x: int(x), open(os.path.join(os.getcwd(), '1\input.txt'), 'r').readlines()))

increments = 0
for index, value in enumerate(ints):
    #print(index, value)
    if index in [0,1,2]:
        continue
    previous = ints[index - 1] + ints[index - 2] + ints[index - 3]
    current = value + ints[index - 1] + ints[index - 2]
    
    if current > previous:
        increments += 1

print(increments)


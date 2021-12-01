import os

ints = list(map(lambda x: int(x), open(os.path.join(os.getcwd(), '1\input.txt'), 'r').readlines()))

increments = 0
for index, value in enumerate(ints):
    #print(index, value)
    if index == 0:
        continue
    
    if value > ints[index - 1]:
        increments += 1

print(increments)


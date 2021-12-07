
input = list(map(lambda x: int(x), open("6/input.txt").read().strip().split(',')))
fishes = [0]*9
for el in input:
    fishes[el] = fishes[el] + 1

#input = [3,4,3,1,2]

for day in range(256):
    to_add = 0
    for i in range(len(fishes)):
        if i == 0:
            to_add = fishes[0]
        else:
            fishes[i-1] = fishes[i]
    fishes[6] += to_add
    fishes[8] = to_add
           

print(sum(fishes))

#1 = 353079
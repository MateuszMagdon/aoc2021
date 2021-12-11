from pprint import pprint

def get_input():
    lines = open("11/input.txt").readlines()
    return [[int(el) for el in line.strip()] for line in lines]

def increase_power(map, x, y):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            try:
                if i >= 0 and j >= 0:
                    map[i][j] += 1
            except:
                continue

def flash(map):
    flashes = 0
    for x, row in enumerate(map):
        for y, col in enumerate(row):
            if col > 9:
                row[y] = -100
                flashes += 1
                increase_power(map, x, y)
    return flashes

def count_negatives(map):
    total = 0
    for row in map:
        for el in row:
            if el < 0:
                total += 1
    return total 

def refresh_val(val):
    return 0 if val < 0 else val

map = get_input()

step = 0
total_flashes = 0
map_size = len(map)*len(map[0])
while total_flashes != map_size:
    map = [[el+1 for el in row] for row in map] # add 1 to each element

    new_flashes = flash(map)
    while new_flashes:
        new_flashes = flash(map)

    total_flashes = count_negatives(map)
    map = [[refresh_val(el) for el in row] for row in map] # negatives back to 0
    step+=1

print(step)
#242

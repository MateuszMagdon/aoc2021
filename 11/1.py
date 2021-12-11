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


def refresh_val(val):
    return 0 if val < 0 else val

map = get_input()

total_flashes = 0
for i in range(100):
    map = [[el+1 for el in row] for row in map] # add 1 to each element

    new_flashes = flash(map)
    while new_flashes:
        total_flashes += new_flashes
        new_flashes = flash(map)
    
    map = [[refresh_val(el) for el in row] for row in map] # negatives back to 0


print(total_flashes)
#1637

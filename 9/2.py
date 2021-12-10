def is_local_min(map, x, y):
    max_x = len(map)-1
    max_y = len(map[0])-1
    val = map[x][y]

    if x > 0:
        if val >= map[x-1][y]:
            return False

    if x < max_x:
        if val >= map[x+1][y]:
            return False

    if y > 0:
        if val >= map[x][y-1]:
            return False

    if y < max_y:
        if val >= map[x][y+1]:
            return False
    return True

def calc_basin_size(map, x, y, start=True):
    max_x = len(map)-1
    max_y = len(map[0])-1

    total = 0
    to_discover=[(x, y)]

    while to_discover:
        el = to_discover.pop()
        x = el[0]
        y = el[1]
        if not start and map[x][y] == 0:
            continue
        start = False

        map[x][y] = 0
        total += 1

        if x > 0 and map[x-1][y] not in [0, 9]:
            to_discover.append((x-1, y))

        if x < max_x and map[x+1][y] not in [0, 9]:
            to_discover.append((x+1, y))

        if y > 0 and map[x][y-1] not in [0, 9]:
            to_discover.append((x, y-1))

        if y < max_y and map[x][y+1] not in [0, 9]:
            to_discover.append((x, y+1))
    
    return total


lines = open("9/input.txt").readlines()
map = [[int(el) for el in line.strip()] for line in lines]

width = len(map[0])
height = len(map)

mins = []
for x in range(height):
    for y in range(width):

        if is_local_min(map, x, y):
            mins.append({'x': x, 'y': y})

basins = []
for min in mins:
    basins.append(calc_basin_size(map, min['x'], min['y']))

basins.sort(reverse=True)
print(basins[0]*basins[1]*basins[2])

#931200

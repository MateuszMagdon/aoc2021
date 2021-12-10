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

def calc_basin_size(map, x, y, mode=0):
    max_x = len(map)-1
    max_y = len(map[0])-1
        
    if mode != 0 and map[x][y] == 0:
        return 0 

    total = 1
    map[x][y] = 0

    if mode != 2 and x > 0:
        if map[x-1][y] < 9:
            total += calc_basin_size(map, x-1, y, 1)

    if mode != 1 and x < max_x:
        if map[x+1][y] < 9:
            total += calc_basin_size(map, x+1, y, 2)

    if mode != 4 and y > 0:
        if map[x][y-1] < 9:
            total += calc_basin_size(map, x, y-1, 3)

    if mode != 3 and y < max_y:
        if map[x][y+1] < 9:
            total += calc_basin_size(map, x, y+1, 4)
    
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

def isLocalMin(map, x, y):
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


lines = open("9/input.txt").readlines()
map = [[int(el) for el in line.strip()] for line in lines]

width = len(map[0])
height = len(map)

total = 0
for x in range(height):
    for y in range(width):

        if isLocalMin(map, x, y):
            total += 1 + map[x][y]

print(total)
#506

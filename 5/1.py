
def parse_input(file_name):
    inputs = []
    for line in open(file_name).readlines():
        splitted = line.split()
        x1, y1 = list(map(lambda x: int(x), splitted[0].split(',')))
        x2, y2 = list(map(lambda x: int(x), splitted[2].split(',')))
        inputs.append([x1, y1, x2, y2])

    return inputs

def mark_lines(map, lines):
    for el in only_horizontal_or_vertical:
        max_x = max(el[0], el[2])
        min_x = min(el[0], el[2])
        for x in range(min_x, max_x+1):
            max_y = max(el[1], el[3])
            min_y = min(el[1], el[3])
            for y in range(min_y, max_y+1):
                map[x][y] += 1

def count_result(map):
    result = 0
    for row in _map:
        for col in row:
            if col > 1:
                result+=1
    return result


inputs = parse_input('5/input.txt')

only_horizontal_or_vertical = list(filter(lambda x: x[0] == x[2] or x[1] == x[3], inputs))

_map = [[0]*1000 for i in range(1000)]
mark_lines(_map, only_horizontal_or_vertical)

print(count_result(_map))

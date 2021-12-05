
def parse_input(file_name):
    inputs = []
    for line in open(file_name).readlines():
        splitted = line.split()
        x1, y1 = list(map(lambda x: int(x), splitted[0].split(',')))
        x2, y2 = list(map(lambda x: int(x), splitted[2].split(',')))
        inputs.append([x1, y1, x2, y2])

    return inputs

def mark_lines(map, lines):
    for el in lines:
        is_diagonal = el[0] != el[2] and el[1] != el[3]
        reverse_x = el[0] > el[2] 
        step_x = -1 if reverse_x else 1
        offset_y = 0
        for x in range(el[0], el[2]+step_x, step_x):
            reverse_y = el[1] > el[3]
            step_y = -1 if reverse_y else 1
            for y in range(el[1]+(offset_y)*step_y, el[3]+step_y, step_y):
                map[x][y] += 1
                if is_diagonal:
                    offset_y += 1
                    break;


def count_result(map):
    result = 0
    for row in _map:
        for col in row:
            if col > 1:
                result+=1
    return result


inputs = parse_input('5/input.txt')

_map = [[0]*1000 for i in range(1000)]
mark_lines(_map, inputs)

print(count_result(_map))



def get_input(filename):
    map = []
    lines = [line.strip().split(',') for line in open(filename).readlines()]
    
    folds = []
    max_x = 0
    max_y = 0
    
    for index, line in enumerate(lines):
        if len(line) == 2:
            lines[index] = [int(el) for el in line]
            if lines[index][0] > max_x:
                max_x = lines[index][0]
            if lines[index][1] > max_y:
                max_y = lines[index][1]
        
        elif len(line[0]) != 0 and len(line) == 1:
            folds.append(line[0].split()[2].split('='))
            folds[-1][1] = int(folds[-1][1])
    
    map = [['.' for x in range(max_x + 1)] for y in range(max_y + 1)]
    for line in lines:
        if len(line) == 2:
            map[line[1]][line[0]] = '#'
    
    return map, folds

def fold_map(map, folds):
    len_horizontal = len(map[0])
    len_vertical = len(map)
    for fold in folds[:1]:
        if fold[0] == 'x':
            max_y = 2*fold[1]
            len_horizontal = fold[1]

            for x in range(len_vertical):
                map[x][fold[1]] = '|'
                for y in range(fold[1]):
                    if map[x][y] == '#' or map[x][max_y-y] == '#':
                        map[x][y] = '#'
                    else:
                        map[x][y] = '.'
                    map[x][max_y-y] = ''
        else:
            max_x = 2*fold[1]
            len_vertical = fold[1]
            
            for y in range(len_horizontal):
                map[fold[1]][y] = '-'
            
            for x in range(fold[1]):
                for y in range(len_horizontal):
                    map[fold[1]][y] = '-'

                    if map[x][y] == '#' or map[max_x-x][y] == '#':
                        map[x][y] = '#'
                    else:
                        map[x][y] = '.'
                    map[max_x-x][y] = ''

def count_dots(map):
    sum = 0
    for x, row in enumerate(map):
        for y, _ in enumerate(row):
            if map[x][y] == '#':
                sum += 1
    return sum

map, folds = get_input('13/input.txt')
fold_map(map, folds)

print(count_dots(map))
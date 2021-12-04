
def count_commons(values, index):
    calc = 0
    
    for value in values:
        if value[index] == '1':
            calc += 1
        else:
            calc -= 1
    return calc


lines = list(map(lambda x: x[:-1], open('3\input.txt').readlines()))


oxygen_lines = lines[:]
index = 0
while len(oxygen_lines) > 1:
    common = count_commons(oxygen_lines, index)
    oxygen_lines = [line for line in oxygen_lines if (common >= 0 and line[index] == '1') or (common < 0 and line[index] == '0')]
    
    index+=1
    
co2_lines = lines[:]
index = 0
while len(co2_lines) > 1:
    common = count_commons(co2_lines, index)
    co2_lines = [line for line in co2_lines if (common < 0 and line[index] == '1') or (common >= 0 and line[index] == '0')]
    
    index+=1

print(int(oxygen_lines[0], 2)* int(co2_lines[0], 2))

#4125600

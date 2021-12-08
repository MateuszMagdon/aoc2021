
#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

# a     1
#b c   2 3
# d     4
#e f   5 6
# g     7

# len:
# 0: 6 => len = 6 & cont 1 ###
# 1: 2 #
# 2: 5 
# 3: 5 => len = 5 & cont 1 ##
# 4: 4 #
# 5: 5 
# 6: 6 => len = 6 ####
# 7: 3 #
# 8: 7 #
# 9: 6 => len = 6 & cont 4 ##

def get_key(val, dict):
    for key, value in dict.items():
         if val == value:
             return key

def superset(pattern, dict, indexes):
    result = False
    for index in indexes:
        result = result or (index in dict and pattern.issuperset(dict[index]))
    
    return result

def not_superset(pattern, dict, indexes):
    result = False
    for index in indexes:
        result = result or (index in dict and not pattern.issuperset(dict[index]))
    
    return result
def decode(patterns, outputs):
    dict = {}
    patterns.sort(key = len)
    for pattern in patterns:
        patter_len = len(pattern)
        if patter_len == 2:
            dict[1] = pattern
        elif patter_len == 3:
            dict[7] = pattern
        elif patter_len == 4:
            dict[4] = pattern
        elif patter_len == 5:
            if superset(pattern, dict, [7]):
                dict[3] = pattern
            elif 4 in dict and len(pattern.intersection(dict[4])) == 3:
                dict[5] = pattern
            else:
                dict[2] = pattern
        elif patter_len == 6:
            if superset(pattern, dict, [4]):
                dict[9] = pattern
            elif superset(pattern, dict, [7]):
                dict[0] = pattern
            else:
                dict[6] = pattern
        elif patter_len == 7:
            dict[8] = pattern
    
    result = 0
    it = 1000
    dict_values = dict.values()
    for output in outputs:
        if output in dict_values:
            result += it * get_key(output, dict)
        else:
            result += it * 6
        it /= 10
        
    return int(result)


lines = [line.split('|') for line in open("8/input.txt").read().strip().split('\n')]

total = 0
for line in lines:
    signal_pattern = []
    output = []
    
    pattern_elements = line[0].split()
    for element in pattern_elements:
        signal_pattern.append(set(element))

    output_elements = line[1].split()
    for element in output_elements:
        output.append(set(element))

    total += decode(signal_pattern, output)

print(total)
#1070188



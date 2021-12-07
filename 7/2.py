import statistics, math
input = list(map(lambda x: int(x), open("7/input.txt").read().strip().split(',')))

target_position = int(math.floor(statistics.mean(input)))
target_position_1 = int(math.ceil(statistics.mean(input)))

cumulative = 0
cumulative_1 = 0
for crab_position in input:
    diff = abs(crab_position - target_position)
    diff_1 = abs(crab_position - target_position_1)
    
    movement = [x for x in range(1, diff + 1)]
    cumulative += sum([x for x in range(1, diff + 1)])
    cumulative_1 += sum([x for x in range(1, diff_1 + 1)])

print(min(cumulative, cumulative_1))


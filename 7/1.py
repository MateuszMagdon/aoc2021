import statistics
input = list(map(lambda x: int(x), open("7/input.txt").read().strip().split(',')))

target_position = int(statistics.median(input))

cumulative = 0
for crab_position in input:
    cumulative += abs(crab_position - target_position)

print(cumulative)

#349812
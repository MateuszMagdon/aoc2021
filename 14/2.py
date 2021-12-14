
from types import resolve_bases


def get_input(filename: str):
    lines = [line.strip() for line in open(filename).readlines()]
    input = lines[0]

    transformations = {}
    for line in lines[2:]:
        elements = line.split(' -> ')
        transformations[elements[0]] = elements[1]

    return input, transformations


def transform(input: list, transformations: dict):
    pairs = {}
    for i in range(len(input)-1):
        if input[i]+input[i+1] in pairs:
            pairs[input[i]+input[i+1]] += 1
        else:
            pairs[input[i]+input[i+1]] = 1

    for i in range(40):
        new_pairs = {}
        for pair in pairs:
            new_pair_left = pair[0]+transformations[pair]
            if new_pair_left in new_pairs:
                new_pairs[new_pair_left] += pairs[pair]
            else:
                new_pairs[new_pair_left] = pairs[pair]

            new_pair_right = transformations[pair] + pair[1]
            if new_pair_right in new_pairs:
                new_pairs[new_pair_right] += pairs[pair]
            else:
                new_pairs[new_pair_right] = pairs[pair]
        pairs = new_pairs

    return pairs


def count_letters(pairs, first_letter, last_letter):
    dict = {first_letter: 1, last_letter: 1}
    for pair in pairs:
        if pair[0] in dict:
            dict[pair[0]] += pairs[pair]
        else:
            dict[pair[0]] = pairs[pair]

        if pair[1] in dict:
            dict[pair[1]] += pairs[pair]
        else:
            dict[pair[1]] = pairs[pair]

    max = 0
    min = dict[first_letter]
    for letter in dict:
        if dict[letter] > max:
            max = dict[letter]
        elif dict[letter] < min:
            min = dict[letter]
    return int((max/2)-(min/2))


input, transformations = get_input('14/input.txt')
transformed_input = transform(input, transformations)
result = count_letters(transformed_input, input[0], input[-1])

print(result)
#2911561572630

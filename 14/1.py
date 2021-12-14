
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
    for i in range(10):
        input_len = len(input)
        for j in range(input_len-1):
            if input[input_len-j-2]+input[input_len-j-1] in transformations:
                input = input[:input_len-j-1] + transformations[input[input_len-j-2]+input[input_len-j-1]] + input[input_len-j-1:]
    return input


def count_letters(input: list):
    dict = {}
    for letter in input:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1

    max = 0
    min = 10000
    for letter in dict:
        if dict[letter] > max:
            max = dict[letter]
        elif dict[letter] < min:
            min = dict[letter]
    return max-min


input, transformations = get_input('14/input.txt')
transformed_input = transform(input, transformations)
result = count_letters(transformed_input)


print(result)
#2657


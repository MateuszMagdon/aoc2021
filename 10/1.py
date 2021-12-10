def check_line(line):
    dic = {'(':')', '[':']', '{':'}', '<':'>' }
    stack = []
    for el in line[:-1]:
        if el in dic:
            stack.append(el)
        else:
            it = stack.pop()
            if dic[it] != el:
                return el

def check_score(it):
    match it:
        case ')': return 3
        case ']': return 57
        case '}': return 1197
        case '>': return 25137
    return 0


total = 0
for index, line in enumerate(open("10/input.txt")):
    line_result = check_line(line)
    print(index, line_result)
    total += check_score(line_result)


print(total)
#370407

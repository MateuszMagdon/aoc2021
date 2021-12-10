import statistics

def check_line(line):
    dic = {'(':')', '[':']', '{':'}', '<':'>' }
    stack = []
    for el in line[:-1]:
        if el in dic:
            stack.append(el)
        else:
            it = stack.pop()
            if dic[it] != el:
                return None #broken line
    
    return stack


scores_dict = {'(':1, '[':2, '{':3, '<':4}
totals = []
for index, line in enumerate(open("10/input.txt")):
    line_result = check_line(line)

    if line_result != None:
        line_score = 0
        for el in reversed(line_result):
            line_score *=5
            line_score += scores_dict[el]
        totals.append(line_score)
    


print(statistics.median(totals))
#3249889609

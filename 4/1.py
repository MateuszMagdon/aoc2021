def playBingo(inputs, tables):
    for input in inputs:
        for table in tables:
            for row in table:
                for index, el in enumerate(row):
                    if el == input:
                        row[index] = str(el)

                    if checkIfWinner(table):
                        return countWinningNumber(table, input)
                         


def checkIfWinner(table):
    winnerCol = [True, True, True, True, True]
    for row in table:
        winnerRow = True
        for col, el in enumerate(row):
            if not isinstance(el, str):
                winnerRow = False
                winnerCol[col] = False
        if winnerRow:
            return True

    return True in winnerCol

def countWinningNumber(table, lastCalled):
    unmarked = 0
    for row in table:
        for col in row:
            if not isinstance(col, str):
                unmarked += col

    print(unmarked*lastCalled)

lines = open("4/input.txt").readlines()

inputs = list(map(int, lines[0][:-1].split(',')))

tables = [[]]
for line in lines[2:]:
    if len(line) > 1:
        tables[-1].append(list(map(int, line[:-1].split())))
    else:
        tables.append([])

print(playBingo(inputs, tables))









#print(tables)

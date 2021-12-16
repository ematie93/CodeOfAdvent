import sys
sys.setrecursionlimit(2050)

with open('puzzle.txt') as f:
    mylist = [line.rstrip('\n') for line in f]



def sonar(puzzle, position, increesedValues = []):
    puzzleLen = len(puzzle) - 1
    if puzzle.index(puzzle[position]) == puzzleLen:
        print("No more data")
        print("There where " + str(len(increesedValues)) + " increesed values")

    else:
        if puzzle[position + 1] > puzzle[position]:
            increesedValues.append(puzzle[position + 1])

        return sonar(puzzle, position + 1, increesedValues)

sonar(mylist, 10)

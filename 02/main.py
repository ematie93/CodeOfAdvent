##########################################
"""
Second exercise in the Advent of Code 2021 Challenge
This exercise is called 
Dive!
Exercise can be found here:
https://adventofcode.com/2021/day/2

"""
import sys
sys.setrecursionlimit(1050)

with open("puzzle.txt", "r") as f:
    mylist = [line.rstrip('\n') for line in f]
    f.close

def deepDive(orderList, order = 0, x = 0, y = 0):

    orderLen = len(orderList)
    #lastItemIndex = orderList.index(orderList[orderLen])
    
    if int(order) == int(orderLen):
        print("No more data")
        print("The Final Position is: " + str(x) + ","+ str(y))
    
    else:
        step = orderList[order].split()
        argument = step[0]

        if argument == "forward":
            x = x + int(step[1])
        elif argument == "up":
            y = y + int(step[1])
        else:
            y = y - int(step[1])

        print(str(x) + " " + str(y))

        return deepDive(mylist, order + 1, x, y)
        

deepDive(mylist)


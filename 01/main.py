##############################
"""
This is the first exercise for Advent of Code Challenge
This exercise is called Sonar Sweep
Exercise can be found here:

https://adventofcode.com/2021/day/1
"""

with open('puzzle.txt') as f:
    mylist = [int(line.rstrip('\n')) for line in f]
    f.close()
######### ITS SOOOOOO IMPORTANT TO CONVERT IT TO INTS, STR COMPARASION COMPARES UNICODE BYTS!!!!!!!!!!!

limit = len(mylist)
countInc = 0

#### Part A
for i in range(1, (limit)):
    
    if int(mylist[i - 1]) <= int(mylist[i]):
        print(str(mylist[i-1])+ " < " +  mylist[i])
        countInc += 1
    else:
        print(str(mylist[i-1])+ " > " +  mylist[i])


##### Part B
print(countInc)

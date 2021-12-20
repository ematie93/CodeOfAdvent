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
mylist2 = []
countInc = 0


#### Part A
for i in range(1, (limit)):
    
    if int(mylist[i - 1]) <= int(mylist[i]):
        countInc += 1

##### Part B
#create new 
for i in range(0, (limit - 1)):
    if len(mylist[i:i+3]) == 3:
        suma = sum(mylist[i:i+3])
        mylist2.append(suma)
limit2 = len(mylist2)
countInc2 = 0

for i in range(1, (limit2)):
    
    if int(mylist2[i - 1]) < int(mylist2[i]):
        countInc2 += 1
  
print(countInc2)


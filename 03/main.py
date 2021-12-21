##############################
"""
This is the third exercise for Advent of Code Challenge
This exercise is called Binary Diagnostic
Exercise can be found here:

https://adventofcode.com/2021/day/3
I admit this one was more complicated than I expected
"""
from collections import Counter
import pandas as pd

with open("puzzle.txt", "r") as f:
    mylist = [line.rstrip('\n') for line in f]
    f.close

data = []
gamma = ""
epsilon = ""


for input in mylist:
    data.append(list(input))
data_df = pd.DataFrame(data)

for i in range(0, 12):
    syntheticSugar = Counter(list(data_df[i])).most_common()
    gamma+=str(int(syntheticSugar[0][0]))
    epsilon+=str(int(syntheticSugar[1][0]))

###Part A
print(int(gamma, 2)*int(epsilon, 2))

#part B
#UnderConstrucction
"""
data_dfB = data_df.copy()

for i in range(0, len(data_dfB.columns)):
    mstcom = (Counter(list(data_dfB[i])).most_common())[0][0]
    for j in range(0, len(data_dfB[0])):
        if data_dfB[i][j] != mstcom:
            data_dfB.drop([i], inplace=True)

print(data_dfB)
"""
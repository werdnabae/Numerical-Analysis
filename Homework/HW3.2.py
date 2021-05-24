from random import *
import numpy as np
import matplotlib.pyplot as plt
import math


oneLine = np.zeros(12)
twoLine = np.zeros(12)
threeLine = np.zeros(12)
fourLine = np.zeros(12)

oneLine[9] = 1444444
oneLine[10] = 1444444
oneLine[11] = 1444444


twoLine[10] = 1444444
twoLine[11] = 1444444

threeLine[11] = 1444444
#initial seeds for random number generation
x1 = 0.2025561954107145
x2 = 0.5262907150065293

for i in range(0, 1444444):
    temp = x2
    x2 = math.fmod(x2 + x1, 1)
    x = x2 # the actual random center being used
    x1 = temp

    
    if (x + 1/20 > 1 or x - 1/20 < 0): # probability with d = 1/10
        oneLine[0] = oneLine[0] +1
    
    if (x + 2/20 > 1 or x - 2/20 < 0): # probability with d = 2/10
        oneLine[1] = oneLine[1] +1

    if (x + 3/20 > 1 or x - 3/20 < 0): # probability with d = 3/10
        oneLine[2] = oneLine[2] +1

    if (x + 4/20 > 1 or x - 4/20 < 0): # probability with d = 4/10
        oneLine[3] = oneLine[3] +1
    
    if (x + 5/20 > 1 or x - 5/20 < 0): # probability with d = 5/10
        oneLine[4] = oneLine[4] +1
    
    if (x + 6/20 > 1 or x - 6/20 < 0): # probability with d = 6/10
        oneLine[5] = oneLine[5] +1
    
    if (x + 7/20 > 1 or x - 7/20 < 0): # probability with d = 7/10
        oneLine[6] = oneLine[6] +1
    
    if (x + 8/20 > 1 or x - 8/20 < 0): # probability with d = 8/10
        oneLine[7] = oneLine[7] +1

    if (x + 9/20 > 1 or x - 9/20 < 0): # probability with d = 9/10
        oneLine[8] = oneLine[8] +1

    x_15_10 = x * 2 - 0.75
    if (x_15_10 + 15/20 > 1 and x_15_10 - 15/20 < 0): # probability with d = 15/10
        twoLine[9] = twoLine[9] +1

    if(x == 0):
        threeLine[10] = threeLine[10] + 1
        fourLine[11] = fourLine[11] + 1

for i in range(0, 12):
    oneLine[i] = oneLine[i] / 1444444 * 100
    twoLine[i] = twoLine[i] / 1444444 * 100
    threeLine[i] = threeLine[i] / 1444444 * 100
    fourLine[i] = fourLine[i] / 1444444 * 100

print(oneLine)
print(twoLine)
print(threeLine)
print(fourLine)

disc = [1/10, 2/10, 3/10, 4/10, 5/10, 6/10, 7/10, 8/10, 9/10, 15/10, 20/10, 30/10]

plt.plot(disc, oneLine, label = '1 line')
plt.plot(disc, twoLine, label = '2 line')
plt.plot(disc, threeLine, label = '3 line')
plt.plot(disc, fourLine, label = '4 line')
plt.legend()
plt.show()
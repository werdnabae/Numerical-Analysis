from random import *
import numpy as np
import matplotlib.pyplot as plt
import math

randX = np.zeros(9) 
randY = np.zeros(9)
randH = np.zeros(9)

rand1 = 0.2025561954107145
rand2 = 0.5262907150065293
rand3 = 0.4017968876832646
rand4 = 0.10272487008673348

maxSum = 0
maxSumIdx = 0
for i in range(0, 9): #creates random points from [-0.8, 0.8] 
    temp = rand2
    rand2 = (rand1 + rand2) % 1
    radn1 = temp
    randX[i] = rand2 * 100

    temp = rand2
    rand2 = (rand1 + rand2) % 1
    radn1 = temp
    randY[i] = rand2 * 100

    temp = rand3
    rand4 = (rand3 + rand4) % 1
    radn3 = temp

    x1 = rand3
    x2 = rand4
    g1 = (math.sqrt(-2 * math.log(x1)) * math.cos(2 * x2 * math.pi ))
    g2 = (math.sqrt(-2 * math.log(x1)) * math.sin(2 * x2 * math.pi ))
    randH[i] = 10 + g1 * 1.777
    print('X =',  randX[i])
    print('Y =',  randY[i])
    print('H =', randH[i])
    print('/')
    summ = randX[i] + randY[i] + randH[i]
    if summ > maxSum:
        maxSum = summ
        maxSumIdx = i
     
print('max index =', maxSumIdx)
order = [5, 0, 1, 2, 3, 4, 6, 7, 8]
dist = 0
for i in range(0, len(order) - 1):
    dist = dist + np.sqrt((randX[order[i+1]] - randX[order[i]])**2 + (randY[order[i+1]] - randY[order[i]])**2 + (randH[order[i+1]] - randH[order[i]])**2)
print(dist)
minDist = dist
T = 45
for i in range(0, 1000000):
    orderTemp = order[:]
    a = randint(1, 8)
    b = randint(1, 8)
    #print(a, b)

    temp = orderTemp[b]
    orderTemp[b] = orderTemp[a]
    orderTemp[a] = temp
    distTemp = 0
    #print(orderTemp)
    for i in range(0, len(order) - 1):
        distTemp = distTemp + np.sqrt((randX[orderTemp[i+1]] - randX[orderTemp[i]])**2 + (randY[orderTemp[i+1]] - randY[orderTemp[i]])**2 + (randH[orderTemp[i+1]] - randH[orderTemp[i]])**2)
    #print('temp', distTemp)
    #print('min dist', minDist)
    T = 45 / (np.log(i) * i)

    if distTemp <= minDist:
        #print('New One Taken')
        order = orderTemp[:]
        minDist = distTemp
    else:
        P = np.exp(-(distTemp - minDist) / T)
        #print('P', P)
        testP = random()
        
        #print('testP', testP)
        if testP < P:
            #print('new Taken')
            order = orderTemp[:]
            minDist = distTemp

print(minDist)   


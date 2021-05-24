from random import *
import numpy as np
import matplotlib.pyplot as plt
import math

randX = np.zeros(16) 
randY = np.zeros(16)
randH = np.zeros(16)

rand1 = 0.2025561954107145
rand2 = 0.5262907150065293
rand3 = 0.4017968876832646
rand4 = 0.10272487008673348

minSum = 99999999999
minSumIdx = 0
for i in range(0, 16): #creates the coordinates of the trees
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
    g1 = (math.sqrt(-2 * math.log(x1)) * math.cos(2 * x2 * math.pi )) # I could also have used numpy.random.normal
    g2 = (math.sqrt(-2 * math.log(x1)) * math.sin(2 * x2 * math.pi ))
    if i % 2 == 0:
        randH[i] = 10 + g1 * 1.777
    else:
        randH[i] = 10 + g2 * 1.777
    print('Tree Number: ',  i)
    print('X =',  randX[i])
    print('Y =',  randY[i])
    print('H =', randH[i])
    print('/')
    summ = randX[i] + randY[i] + randH[i]
    if summ < minSum:
        minSum = summ
        minSumIdx = i
     
print('Min Tree =', minSumIdx)

order = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
dist = 0

for i in range(0, len(order) - 1): # this is calculating the distance of the initial order
    dist = dist + np.sqrt((randX[order[i+1]] - randX[order[i]])**2 + (randY[order[i+1]] - randY[order[i]])**2 + (randH[order[i+1]] - randH[order[i]])**2)
print(dist)

minDist = dist
T = 45 # kind of arbitrary T
for i in range(0, 10000):
    orderTemp = order[:]
    a = randint(1, 15)
    b = randint(1, 15)
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
print(order)
print(minDist)   


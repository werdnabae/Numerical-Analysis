from random import *
import numpy as np
import matplotlib.pyplot as plt
import math

bestAngle = 0

rand1 = 0.2025561954107145
rand2 = 0.5262907150065293

#empty array to be used for calculating area
randX = np.zeros(100000) 
randY = np.zeros(100000)

for i in range(0, 100000): #creates random points from [-0.8, 0.8] 
    temp = rand2
    rand2 = (rand1 + rand2) % 1
    radn1 = temp
    #randX[i] = rand2 * 1.6 - 0.8
    randX[i] = random() * 2 - 1
    temp = rand2
    rand2 = (rand1 + rand2) % 1
    radn1 = temp
    #randY[i] = rand2 * 1.6 - 0.8
    randY[i] = random() * 2.5 - 1
alpha = 0
CenterX = 0
CenterY = 0
count = 0


T = 50
maxCount = 800

for i in range(1, 2): # Monte carlo will be done 1000 times

    check = 1
    while check ==1: # while loop used to make sure that x, y > 0 and alpha is in between -pi/2 and pi/2
        # prospective changes in the state 
        changeAlpha = random() *(np.pi / 100) - np.pi / 200
        changeX = (random() * 0.016 - 0.008)*20
        changeY = (random() * 0.016 - 0.008)*20

    
        # prospective new states
        tempAlpha = .41#alpha + changeAlpha
        tempCenterX = 37#CenterX + changeX
        tempCenterY = .47#CenterY + changeY

        if (tempAlpha < 1.57 and tempAlpha >0): # 
            check = 0

    print('Center X =', tempCenterX)
    print('Center Y =', tempCenterY)
    print('tempAlpha =', tempAlpha)
    

    def checkPetal(x, y, alpha):
        r = np.sqrt(x**2 + y**2)
        theta = np.arctan((abs(y)/(abs(x))))
        if (abs(r) < np.sin(2*theta + .1)):
            return 1
        return 0
    def checkHeart(x, y): 
        if (x**2 + (y - (x**(2/3)))**2) < (1/2):
            return 1
        return 0
    count = 0
    for i in range(0, 10000):

        ch1 = checkPetal(randX[i] - tempCenterX, randY[i] - tempCenterY, tempAlpha) # check if the point is in the petal
        ch2 = checkHeart(randX[i], randY[i]) # check if he point is in the heart
        if ch1 * ch2 == 1:
            count = count+1
    """
    # Metropolis
    print(count)
    if count > maxCount: # if this new state is better, take the new state
        print('take new one')
        maxCount = count
        centerX = tempCenterX
        centerY = tempCenterY
        alpha = tempAlpha
    else: # if the state is not better, see if you will take it using a probablity
        P = np.exp((count - maxCount) / T)
        #print('difference', (count - maxCount) / T)
        print('P', P)
        testP = random()
        print('test P', testP)
        if testP < P:
            centerX = tempCenterX
            centerY = tempCenterY
            alpha = tempAlpha
            maxCount = count
            print('new Max =', maxCount)
    """
    print('/')

print(maxCount)

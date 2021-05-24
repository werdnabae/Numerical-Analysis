from random import *
import numpy as np
import matplotlib.pyplot as plt

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
    randX[i] = random() * 1.6 - 0.8
    temp = rand2
    rand2 = (rand1 + rand2) % 1
    radn1 = temp
    #randY[i] = rand2 * 1.6 - 0.8
    randY[i] = random() * 1.6 - 0.8



diag = 0.6123724357 # length from center of the box to upper right corner
baseAngle = 0.6154797087 # angle from center of the box to upper right corner

# Starting values to be used
alpha = 0.00001 
CenterX = 0
CenterY = 0

maxCount = 2290 # The approximate area at the starting values
T = 20 # T value to be used in the monte carlo, found by making 10 E(y) and take the average of E(y) – E(x)

for i in range(1, 1001): # Monte carlo will be done 1000 times
    check = 1
    while check ==1: # while loop used to make sure that x, y > 0 and alpha is in between -pi/2 and pi/2
        # prospective changes in the state 
        changeAlhpa = (random() * (np.pi / 100) - np.pi / 200)*2 
        changeX = (random() * 0.016 - 0.008)*20
        changeY = (random() * 0.016 - 0.008)*20

        # prospective new states
        tempAlpha = alpha + changeAlhpa
        tempCenterX = CenterX + changeX
        tempCenterY = CenterY + changeY

        if(tempCenterX > 0 and tempCenterY > 0 and abs(tempAlpha) < 1.57): # 
            check = 0
    
    print('Center X =', tempCenterX)
    print('Center Y =', tempCenterY)
    print('tempAlpha =', tempAlpha)
    
    # creates the coordinates of the box with alpha = 0 at the new x and y
    
    # upper right 
    urY = diag * np.sin(baseAngle) + tempCenterX
    urX = diag * np.cos(baseAngle) + tempCenterY

    # upper left
    ulY = urY
    ulX = urX - 1

    # lower left
    llY = ulY - 0.7071067812
    llX = ulX

    # lower right
    lrY = llY
    lrX = urX

    # finds the coordinates of the box, now rotated around the center of the box with angle alpha
    rURX = (urX - tempCenterX) * np.cos(tempAlpha) - (urY - tempCenterY) * np.sin(tempAlpha) + tempCenterX
    rURY = (urX - tempCenterX) * np.sin(tempAlpha) + (urY - tempCenterY) * np.cos(tempAlpha) + tempCenterY

    rULX = (ulX - tempCenterX) * np.cos(tempAlpha) - (ulY - tempCenterY) * np.sin(tempAlpha) + tempCenterX
    rULY = (ulX - tempCenterX) * np.sin(tempAlpha) + (ulY - tempCenterY) * np.cos(tempAlpha) + tempCenterY

    rLLX = (llX - tempCenterX) * np.cos(tempAlpha) - (llY - tempCenterY) * np.sin(tempAlpha) + tempCenterX
    rLLY = (llX - tempCenterX) * np.sin(tempAlpha) + (llY - tempCenterY) * np.cos(tempAlpha) + tempCenterY

    rLRX = (lrX - tempCenterX) * np.cos(tempAlpha) - (lrY - tempCenterY) * np.sin(tempAlpha) + tempCenterX
    rLRY = (lrX - tempCenterX) * np.sin(tempAlpha) + (lrY - tempCenterY) * np.cos(tempAlpha) + tempCenterY

    # finds the slopes of the 4 lines that represent the box
    m1 = (rURY - rULY) / (rURX - rULX)
    m2 = (rULY - rLLY) / (rULX - rLLX)
    m3 = (rLLY - rLRY) / (rLLX - rLRX)
    m4 = (rLRY - rURY) / (rLRX - rURX)

    # functions to be used to see if random points are in the box or in the rose
    def checkLess(m, x1, y1, x, y): 
        if((y - y1) < (m * (x - x1))):
            return 1
        return 0
    def checkGreater(m, x1, y1, x, y): 
        if((y - y1) > (m * (x - x1))):
            return 1
        return 0
    def checkRose(x, y):
        if (x**2 + y**2)**3 < 4 * (x**2) * (y**2):
            return 1
        return 0

    count = 0

    if tempAlpha > 0: # checking the points if alpha is positive
        for i in range(0, 10000):
            #print(randX[i])
            #print(randY[i])
            ch1 = checkLess(m1, rURX, rURY, randX[i], randY[i])

            ch2 = checkGreater(m2, rULX, rULY, randX[i], randY[i])

            ch3 =  checkGreater(m3, rLLX, rLLY, randX[i], randY[i])

            ch4 = checkLess(m4, rLRX, rLRY, randX[i], randY[i])

            ch5 = checkRose(randX[i], randY[i])

            if((ch1 * ch2 * ch3 * ch4 * ch5) == 1):
                count = count + 1
                #print('000')
            #print('/')
    if tempAlpha < 0: # checking the points if alpha is negative
        for i in range(0, 10000):
            #print(randX[i])
            #print(randY[i])
            ch1 = checkLess(m1, rURX, rURY, randX[i], randY[i])

            ch2 = checkLess(m2, rULX, rULY, randX[i], randY[i])

            ch3 =  checkGreater(m3, rLLX, rLLY, randX[i], randY[i])

            ch4 = checkGreater(m4, rLRX, rLRY, randX[i], randY[i])

            ch5 = checkRose(randX[i], randY[i])

            if((ch1 * ch2 * ch3 * ch4 * ch5) == 1):
                count = count + 1
                #print('000')
            #print('/')
    print(count) # number of points inside the box and the rose
    
    # Monte Carlo portion

    if count > maxCount: # if this new state is better, take the new state
        print('take new one')
        maxCount = count
        centerX = tempCenterX
        centerY = tempCenterY
        alpha = tempAlpha
        maxCount = count
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
    print('/')

# Final parameters   
print('center x = ', centerX)
print('center y = ', centerY)
print('alpha', alpha)
print(maxCount)


area = (count / 100000) * 2.56
print(area)

# Plots the box
plt.plot(rURX, rURY, 'o')
plt.plot(rULX, rULY, 'o')
plt.plot(rLLX, rLLY, 'o')
plt.plot(rLRX, rLRY, 'o')
plt.show()
from random import *
import numpy as np
import matplotlib.pyplot as plt

randX = np.zeros(10000) 
randY = np.zeros(10000)
randAngle = np.zeros(10000)

rand1 = 0.2025561954107145
rand2 = 0.5262907150065293

def fx(x, m, b): #this is the function f(x)
    y = (4 * (x**2) * (m * x + b)**2) - (x**2 + (m * x + b)**2)**3
    return y #returns the value of f(x)

def bisectionMethod (A, B, m, b, count): 

    x = (A + B)/2 #defintion of xn according to the bisection method
    if abs(fx(x, m, b)) <= 0.005: #checks the the error is less than 
        return x #returns the x value
    if count >= 100:
        return 0
    if (fx(A, m, b) * fx(x, m, b)) >=0:
        return bisectionMethod(x, B, m, b, count + 1) #eliminates the left side of x using recursion
    if (fx(B, m, b) * fx(x, m, b)) >= 0:
        return bisectionMethod(A, x, m, b, count + 1) #eliminates the right side of x using recursion
    
count = 0
for i in range(0, 10000): #creates random points from [-0.8, 0.8] 

    randX[i] = random() * 2 - 1
    randY[i] = random() * 2 - 1
    randAngle[i] = random() * np.pi - np.pi/2

    temp = rand2
    rand2 = (rand1 + rand2) % 1
    rand1 = temp
    randX[i] = rand2 * 2 - 1


    temp = rand2
    rand2 = (rand1 + rand2) % 1
    radn1 = temp
    randY[i] = rand2 * 2 - 1


    temp = rand2
    rand2 = (rand1 + rand2) % 1
    radn1 = temp
    randAngle[i] = rand2 * 2 - 1
    
    Y = 0.25 * np.sin(randAngle[i])
    X = 0.25 * np.cos(randAngle[i])
    """
    print('X', randX[i])
    print('Y', randY[i])
    print(randAngle[i])
    """

    rEndX = randX[i] + X
    rEndY = randY[i] + Y
    lEndX = randX[i] - X
    lEndY = randY[i] - Y
    """
    print(rEndX)
    print(rEndY)
    print(lEndX)
    print(lEndY)
    """
    m = (rEndY - lEndY) / (rEndX - lEndX)
    #print('m', m)
    b = m * -randX[i] + randY[i]
    #print('b', b)

    checkRoot = bisectionMethod(lEndX, rEndX, m, b, 0)
    #print('root', checkRoot)
    #print('/')
    if (checkRoot != 0):
        count = count + 1

print(count)


import math
import numpy as np
from random import *


xrandom = [] #creates an empty list for the x coordinates of the Monte Carlo simulation
yrandom = [] #creates an empty list for the y coordinates of the Monte Carlo simulation

for x in range(0, 1000000): #generates 100 million random x and y coordinates within the range [-0.5, 1]
    xrandom.append(-1 + random()*(2)) 
    yrandom.append(1/26 + random()*(25/26))

def f(x): #this is the function f(x)
    y = 1/(1 + 25*x**2)
    return y #returns the value of f(x)
x = np.arange(0.3, 0.5, 0.1)
x1 = np.arange(0, 0.5, 0.1)

count = 0
for i in range(len(xrandom)): #checks if the coordinates are inside of the kidney
    #if the left side minus the right side is negative, then the coordinate is inside of the kidney
    if (yrandom[i] <= f(xrandom[i])): 
        count = count+ 1 #adds a count if the point is inside the kidney

areaf = (count/len(xrandom)) * (2*25/26)
print(areaf)

for i in x:
    m = -1/i
    for j in x1:
        if (abs(1 + m*j - f(j)) <= 0.00005):
            slope = m
            break

edgePoint = -25/26/slope
height = 1 - 1/26
area = edgePoint * height
print(area)
print(areaf - area)
 
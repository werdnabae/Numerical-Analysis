import math
from random import *
import time
import numpy as np


x = [] #creates an empty list for the x coordinates of the Monte Carlo simulation
y = [] #creates an empty list for the y coordinates of the Monte Carlo simulation

for i in range(0, 10000): #generates 100 million random x and y coordinates
    x.append(-0.8 + random()*(1.6)) #generates from -2 to 2
    y.append(-0.8 + random()*(1.6)) #generates from -2 to 3
count = 0
for i in range(len(x)): #checks if the coordinates are inside both the heart and disk
    if (x[i]**2 +y[i]**2)**3 < (4*(x[i]**2)*(y[i]**2)): 
        count = count+ 1 #adds a count if the point is inside 
area = count /len(x) * 2.56
print(area)

sections = 1000000
area = 0
for i in range(0, sections):
    a = math.pi * 2 /sections * i 
    b = math.pi * 2 /sections * (i+1)
    fa = 1/2* (np.sin(2*a))**2
    fb = 1/2* (np.sin(2*b))**2
    area = area + (b-a)*1/2*(fa +fb)

print(area) # does not matter if go from 0 to pi/2 or from 0 to 2pi

    
    
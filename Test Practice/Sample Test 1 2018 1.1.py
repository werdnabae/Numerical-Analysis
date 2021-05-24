from random import *
import math
import time

xrandom = [] #creates an empty list for the x coordinates of the Monte Carlo simulation
yrandom = [] #creates an empty list for the y coordinates of the Monte Carlo simulation

for x in range(0, 1000000): #generates 100 million random x and y coordinates within the range 
    xrandom.append(random()*(8)) 
    yrandom.append(random()*(4))

count = 0
for i in range(len(xrandom)): #checks if the coordinates are inside of the kidney
    t = math.sqrt(yrandom[i])
    negt = -t
    """
    print(t)
    print(xrandom[i])
    print(yrandom[i])
    print((t**5 - 4*(t**3)))
    print((negt**5 - 4*(negt**3)))
    """
    if(xrandom[i] >= (t**5 - 4*(t**3)) and  xrandom[i] <= (negt**5 - 4*(negt**3))):
        count = count + 1

area = (count/len(xrandom)*64)
print(area)
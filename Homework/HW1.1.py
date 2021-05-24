from random import *
import math
import time

startTime = time.time() #records the time when the program starts executing
xrandom = [] #creates an empty list for the x coordinates of the Monte Carlo simulation
yrandom = [] #creates an empty list for the y coordinates of the Monte Carlo simulation

for x in range(0, 100000000): #generates 100 million random x and y coordinates within the range [-0.5, 1]
    xrandom.append(-.5 + random()*(1.5)) 
    yrandom.append(-.5 + random()*(1.5))

count = 0 
for i in range(len(xrandom)): #checks if the coordinates are inside of the kidney
    #if the left side minus the right side is negative, then the coordinate is inside of the kidney
    if (((xrandom[i]**2 + yrandom[i]**2)**2 - xrandom[i]**3 - yrandom[i]**3) <= 0): 
        count = count+ 1 #adds a count if the point is inside the kidney

# calculates the area based off of the ratio of particles inside the kidney times the area where the points were generated
areaKidney = (count/len(xrandom)) * 2.25  

circleRadius = 1/math.sqrt(2)/2

areaCircle = circleRadius**2 * math.pi #calculates the area of the maximum circle
remainingKidney = areaKidney - areaCircle #the area of the remaining kidney is the kidney area minus the circle

endTime = time.time() #records the time when the program stops
print("Remaining kidney area:", remainingKidney, "units squared")

print("Execution time:", endTime - startTime, "seconds") #prints the time in seconds taken for the program to execute
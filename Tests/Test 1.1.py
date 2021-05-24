import math
from random import *
import time

startTime = time.time() #records the time when the program starts executing

x = [] #creates an empty list for the x coordinates of the Monte Carlo simulation
y = [] #creates an empty list for the y coordinates of the Monte Carlo simulation

for i in range(0, 100000000): #generates 100 million random x and y coordinates
    x.append(-2 + random()*(4)) #generates from -2 to 2
    y.append(-2 + random()*(5)) #generates from -2 to 3

count = 0
for i in range(len(x)): #checks if the coordinates are inside both the heart and disk
    if (x[i]**2 + (y[i] - math.sqrt(abs(x[i])))**2 <= 2 and (x[i]**2 + y[i]**2 <= 2)): 
        count = count+ 1 #adds a count if the point is inside 

# calculates the area based off of the ratio of particles inside both figures times the area where the points were generated
area = (count/len(x)) * 20 
print(area)

endTime = time.time() #records the time when the program stops
print("Execution time:", endTime - startTime, "seconds") #prints the time in seconds taken for the program to execute
from random import *
import numpy as np
import matplotlib.pyplot as plt
import math

# Initial values
a = 8
vo = 20
vb = 30
b = 0 # starting off with test angle 0

h = 0.01 # spacing of the x values
x =  np.arange(-8, 8 + h, h) # x values

y = np.zeros(len(x) + 1) # y values, all set to 0 to start


T = 0.04 # Initial tolerance, to be used in metropolis
bestB = b # sets the best distance as 0 to start with
bestDist = 18 # distance when beta = 0

for j in range(0, 1000):

    bTemp = bestB + random() * 0.2 - 0.1 # small change in beta
    
    distTemp = 0

    for i in range(0, len(x)): # solve the differential equation using forward euler

        y[i+1] = y[i] + h * ((2/3) * (1 - ((x[i]**2) / (8**2))) / np.cos(bTemp) + np.sin(bTemp) / np.cos(bTemp))
        
        distTemp = distTemp + np.sqrt(h**2 + (y[i+1] - y[i])**2) # calculates the distance between each small increase
    
    
    if distTemp < bestDist: # if this new state is better, take the new state 
        bestDist = distTemp
        bestB = bTemp
    else: # if the state is not better, see if you will take it using a probablity
        P = np.exp(-(distTemp - bestDist) / T) # probability of accepting new state
        testP = random() #Test P to see if the new state will be accepted
        #print('P', P)
        #print('testP', testP)
        if testP < P:
            bestDist = distTemp
            bestB = bTemp

print('End beta', bestB)
print('End distance', bestDist)
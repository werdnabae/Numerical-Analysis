import math
import matplotlib.pyplot as plt
import numpy as np

h = .001
x = np.arange(0, 1+h, h) # creates x values

y = np.zeros(len(x)) # preallocate v values

bestInitial = 0
for i in range(1, 1000):
    y = np.zeros(len(x))
    y[0] = i/1000
    for j in range(0, len(x)-1):
        y[j+1] = y[j] - h * np.exp(-x[j])*(y[j]**(1/2))
    
    if(abs(y[len(y)-1]) < 0.00001):
        bestInitial = y[0]
        break
print('Beta = 1', bestInitial)

bestInitial = 0
for i in range(1, 1000):
    y = np.zeros(len(x))
    y[0] = i/1000
    for j in range(0, len(x)-1):
        y[j+1] = y[j] - h * np.exp(-10 * x[j])*(y[j]**(1/2))
    if(abs(y[len(y)-1]) < 0.0001):
        bestInitial = y[0]
        break
print('Beta = 10', bestInitial)

bestInitial = 0
for i in range(1, 2):
    y = np.zeros(len(x))
    y[0] = .23
    for j in range(0, len(x)-1):
        y[j+1] = y[j] - h * np.exp(-0.1 * x[j])*(y[j]**(1/2))
    print(y[len(y)-1])
    if(abs(y[len(y)-1]) < 0.0001):
        bestInitial = y[0]
        break
print('Beta = 0.1', bestInitial)
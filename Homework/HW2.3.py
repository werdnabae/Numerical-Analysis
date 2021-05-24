import math
import matplotlib.pyplot as plt
import numpy as np

#initial seeds for random number generation
x1 = 0.2025561954107145
x2 = 0.5262907150065293

xrandom = [] # Empty list to contain all random values that are uniformly distributed
value1 = [1000000] #initial value of portfolio
value2 = [1000000]
value3 = [1000000]

for x in range(0, 260): #generating random numbers from 0 to 1 using "poor man's method"
    temp = x2
    x2 = math.fmod(x2 + x1, 1)
    xrandom.append(x2)
    x1 = temp

for i in range(0, len(xrandom), 2): #creates a list of portfolio value over days for part 1
    
    # Normal distributed values using Box-Muller transform
    fee1 = 0
    fee2 = 0
    x1 = xrandom[i]
    x2 = xrandom[i+1]
    g1 = (math.sqrt(-2 * math.log(x1)) * math.cos(2 * x2 * math.pi ))
    g2 = (math.sqrt(-2 * math.log(x1)) * math.sin(2 * x2 * math.pi ))
    normal1 = (1.002021 + g1 * 0.001984)
    normal2 = (1.002021 + g2 * 0.001984)

    if normal1 > 1: #Adds fee if there is profit
        fee1 = 0.01111 * (normal1 - 1) * value1[i]
    value1.append(value1[i]*normal1 - fee1)

    if normal2 > 1: #Adds fee if there is profit
        fee2 = 0.01111 * (normal2 - 1) * value1[i+1]   
    value1.append(value1[i+1]*normal2 -fee2)


for i in range(0, len(xrandom), 2): #creates a list of portfolio value over days for part 2

    # Normal distributed values using Box-Muller transform
    fee1 = 0
    fee2 = 0
    x1 = xrandom[i]
    x2 = xrandom[i+1]
    g1 = (math.sqrt(-2 * math.log(x1)) * math.cos(2 * x2 * math.pi ))
    g2 = (math.sqrt(-2 * math.log(x1)) * math.sin(2 * x2 * math.pi ))
    normal1 = (0.997979 + g1 * 0.004444)
    normal2 = (0.997979 + g2 * 0.004444)

    if normal1 > 1: #Adds fee if there is profit
        fee1 = 0.01111 * (normal1 - 1) * value1[i]
    value2.append(value2[i]*normal1 - fee1)

    if normal2 > 1: #Adds fee if there is profit
        fee2 = 0.01111 * (normal2 - 1) * value1[i+1]   
    value2.append(value2[i+1]*normal2 -fee2)

for i in range(0, len(xrandom), 2): #creates a list of portfolio values over days for part 3 (no performance fee)
    
    # Normal distributed values using Box-Muller transform
    x1 = xrandom[i]
    x2 = xrandom[i+1]
    g1 = (math.sqrt(-2 * math.log(x1)) * math.cos(2 * x2 * math.pi ))
    g2 = (math.sqrt(-2 * math.log(x1)) * math.sin(2 * x2 * math.pi ))
    normal1 = (1.002021 + g1 * 0.001984)
    normal2 = (1.002021 + g2 * 0.001984)
 
    value3.append(value3[i]*normal1)
    value3.append(value3[i+1]*normal2)

#prints portfolio values at the end
print(value1[260])
print(value2[260])
print(value3[260])

# Plots portfolio values over days for all parts
plt.plot(value1, label = 'Part 1', color = 'red')
plt.plot(value2, label = 'Part 2')
plt.plot(value3, label = 'Part 3', color = 'green')

plt.xlabel('days')
plt.ylabel('Portfolio Value (dollars)')
plt.title('Portfolio Timeline')
plt.legend()
plt.show()
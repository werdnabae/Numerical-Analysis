from random import *
import math
import time
import matplotlib.pyplot as plt

xrandom = []
for x in range(0, 300000000): #generates 200 million random x and y coordinates within the range [-0.5, 1]
    xrandom.append(random()) 

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0

for i in range(0, len(xrandom)): #generates 200 million random x and y coordinates within the range [-0.5, 1]
    if xrandom[i] <= 0.1: 
        count1 = count1 + 1
    if xrandom[i] <= 0.2 and xrandom[i] > 0.1: 
        count2 = count1 + 1
    if xrandom[i] <= 0.3 and xrandom[i] > 0.2: 
        count3 = count1 + 1
    if xrandom[i] <= 0.4 and xrandom[i] > 0.3: 
        count4 = count4 + 1
    if xrandom[i] <= 0.5 and xrandom[i] > 0.4: 
        count5 = count5 + 1
    if xrandom[i] <= 0.6 and xrandom[i] > 0.5: 
        count6 = count6 + 1
    if xrandom[i] <= 0.7 and xrandom[i] > 0.6: 
        count7 = count7 + 1
    if xrandom[i] <= 0.8 and xrandom[i] > 0.7: 
        count8 = count8 + 1
    if xrandom[i] <= 0.9 and xrandom[i] > 0.8: 
        count9 = count9 + 1
    if xrandom[i] <= 1 and xrandom[i] > 0.9:
        count10 = count10 + 1

print("[0 0.1]", count1)    
print("[0.1 0.2]", count2) 
print("[0.2 0.3]", count3) 
print("[0.3 0.4]", count4) 
print("[0.4 0.5]", count5) 
print("[0.5 0.6]", count6) 
print("[0.6 0.7]", count7) 
print("[0.7 0.8]", count8) 
print("[0.8 0.9]", count9) 
print("[0.9 1]", count10) 

normal = []

for i in range(0, len(xrandom), 2):
    x1 = xrandom[i]
    x2 = xrandom[i+1]
    g1 = (math.sqrt(-2 * math.log(x1)) * math.cos(2 * x2 * math.pi ))
    g2 = (math.sqrt(-2 * math.log(x1)) * math.sin(2 * x2 * math.pi ))
    normal.append(10 + g1 * 5)
    normal.append(10 + g2 * 5)

plt.hist(normal, bins = 10000)
plt.show()
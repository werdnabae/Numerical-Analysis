import math
import numpy as np

h = -0.01
t = [0]
y = np.arange(8.888, 0, h) #


for i in range(0, len(y) - 1): 
    t.append(t[i] + 0.01*math.pi*(15.555-1/4*y[i])**2/-(-1.984*math.sqrt(y[i])))
    

t.append(t[len(y)-1] + 0.008*math.pi*(15.555-1/4*0.008)**2/-(-1.984*math.sqrt(0.008)))

print(t[len(y)])

t2 = [0]
for i in range(0, len(y) - 1): 
    t2.append(t2[i] + 0.01*math.pi*(13.333+1/4*y[i])**2/-(-1.984*math.sqrt(y[i])))

t2.append(t2[i] + 0.008*math.pi*(13.333+1/4*0.008)**2/-(-1.984*math.sqrt(0.008)))
print(t2[len(y)])    

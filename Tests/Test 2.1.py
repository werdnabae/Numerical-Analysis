import matplotlib.pyplot as plt
import math
import numpy as np
import time

startTime = time.time() #records the time when the program starts executing

h = 1 # h value
x = np.arange(0.0, 45 + h, h) # set of t values from [0, 25], with 0.001 spacing
y = [1949] # Initial value for Forward Euler
y1 = [1949] # Initial value for RG

for i in range(0, len(x)- 1): # Finds P values using Forward Euler
    y.append(y[i] + h * (-1.444E-5)*y[i]*(1000 - y[i]))

for i in range(0, len(x) - 1): # Finds P values using Rugge-Kutta
    k1 = (-1.444E-5)*(y1[i])*(1000 - y1[i])
    k2 = (-1.444E-5)*(y1[i] + 1/2 * h * k1)*(1000 - (y1[i] + 1/2 * h * k1))
    k3 = (-1.444E-5)*(y1[i] + 1/2 * h * k2)*(1000 - (y1[i] + 1/2 * h * k2))
    k4 = (-1.444E-5)*(y1[i] + h * k3)*(1000 - (y1[i] + h * k3))
    y1.append(y1[i]+1/6*h * (k1 + 2*k2 + 2*k3 + k4))
    print(y[i+1])
    print(y1[i+1])
    print('/')

# Creates plot of the solutions
plt.plot(x, y, label = 'Forward')
plt.text(1, 1, 'h')
plt.plot(x, y1, label = 'RG')
plt.legend(loc = 'upper left')
plt.xlabel('t')
plt.ylabel('P(t)')
plt.title('P(t) vs t')
plt.show()

endTime = time.time() #records the time when the program stops
print("Execution time:", endTime - startTime, "seconds") #prints the time in seconds taken for the program to execute
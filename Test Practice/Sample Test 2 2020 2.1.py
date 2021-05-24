import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.optimize import curve_fit

h = 0.01
x = np.arange(0.0, 0.5 + h, h) 
y = [1]

x1 = []
y1 = []
for i in range(0, len(x)-1): # set of values for forward euler
    y.append(y[i] + h*(x[i] + y[i] + x[i]*y[i]))
"""
plt.plot(x, y)
plt.show()
"""
for i in range(0, len(x)): # set of values for forward euler
    if x[i] == 0.1 or x[i] == 0.2 or x[i] == 0.3 or x[i] == 0.4 or x[i] == 0.5:
        x1.append(x[i])
        y1.append(y[i])
 
print(x1)
print(y1)

def poly4(x, a0, a1, a2, a3, a4): # need x to come first
    return a0 + a1*x + a2*(x**2) + a3*(x**3) + a4*(x**4)

fit, pcov = curve_fit(poly4, x1, y1)
print('a0 =', fit[0])
print('a1 =', fit[1])
print('a2 =', fit[2])
print('a3 =', fit[3])
print('a4 =', fit[4])

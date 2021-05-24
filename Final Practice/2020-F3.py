import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

#initial seeds for random number generation
x1 = 0.2025561954107145
x2 = 0.5262907150065293

change1 = np.random.normal(0.005, 0.015, 60)
change2 = np.random.normal(0.01, 0.013, 190)

dow = np.zeros(251)
dow[0] = 24600

for i in range(0, 60):
    dow[i + 1] = dow[i] * (1+ change1[i])

for i in range(60, 250):
    dow[i + 1] = dow[i] * (1+change2[i-60])

def summerFit(x, a, b): # need x to come first
    y = a * np.exp(b*x)
    return y
def poly4(x, a0, a1, a2, a3, a4): # need x to come first
    return a0 + a1*x + a2*(x**2) + a3*(x**3) + a4*(x**4)

x = [10, 20, 30, 40, 50, 60]
y = [dow[10], dow[20], dow[30], dow[40], dow[50], dow[60]]
print(x)
print(y)
fit, pcov = curve_fit(summerFit, x, y, p0 = (2.5E4, 0.006)) # have to iclude the p0, that is the initial guess
print(fit)
plt.plot(dow)
plt.show()
import numpy as np
import matplotlib.pyplot as plt

h = .001
k = 1/3

x = np.arange(0, 100, h) # creates x values

y = np.zeros(len(x)) # preallocate y values


for i in range(len(x)-1, 0, -1):
    #Use y[i] - h * f(x,y) instead of y[i] + h * f(x,y) because technically, h is negative
    y[i-1] = y[i] - h * ((y[i]/x[i]) - k * np.sqrt(1 + (y[i]/x[i])**2)) # determines next y value using foward euler
    print(x[i-1])
    print(y[i-1])


#plots graph y vs x
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
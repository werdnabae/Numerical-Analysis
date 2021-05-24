import matplotlib.pyplot as plt
import math
import numpy as np

h = 1E-4
xval = np.arange(0, 1, h) # creates x values
yval = np.ones(len(xval)) # preallocate v values

def f(c, x, y): #this is the function f(x)
    return np.exp(-c) - c - (x**3) - (y**3)

def bisectionMethod (A, B, x, y): 
    a = A
    b = B
    c = (a + b)/2 #defintion of xn according to the bisection method
    
    if abs(f(c, x, y)) <= 0.00005: #checks the the error is less than 
        return c #returns the x value
    if (f(a, x, y) * f(c, x, y)) >=0:
        return bisectionMethod(c, b, x, y) #eliminates the left side of x using recursion
    if (f(b, x, y) * f(c, x, y)) >= 0:
        return bisectionMethod(a, c, x, y) #eliminates the right side of x using recursion

for i in range(0, len(xval)-1):
    yval[i+1] = yval[i] + h * bisectionMethod(-5, 5, xval[i], yval[i])

plt.plot(xval, yval)
plt.show()
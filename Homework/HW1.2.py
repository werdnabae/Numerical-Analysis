import math
import time

startTime = time.time() #records the time when the program starts executing

def fx(x): #this is the function f(x)
    y = 2.021 ** (-x**3) - x**3 * math.cos(x**4) - 1.984
    return y #returns the value of f(x)

a = -1
b = -0.6

def bisectionMethod (A, B): 
    a = A
    b = B
    x = (a + b)/2 #defintion of xn according to the bisection method
    if abs(fx(x)) <= 0.00005: #checks the the error is less than 
        return x #returns the x value
    if (fx(a) * fx(x)) >=0:
        return bisectionMethod(x, b) #eliminates the left side of x using recursion
    if (fx(b) * fx(x)) >= 0:
        return bisectionMethod(a, x) #eliminates the right side of x using recursion

ans1 = bisectionMethod(a, b) #calls the bisection method function to find a root at x1 which is between a and b
print("The root at x1 is", ans1)

def newtonMethod(x0):#Newton's method for finding roots
    x = x0
    if abs(fx(x)) <= 0.00005: #checks the the error is less than 
        return x #returns the x value
    return newtonMethod(x - (fx(x)/ derivativeCD(x))) #iterates Newton's Method until solution is found

def derivativeCD(x): #calculating the derivative using Central Difference
    return (fx(x + 1E-6)- fx(x - 1E-6))/(2E-6) #h value of 1E-6 is used

ans2 = newtonMethod(1.2) #calls the newtonMethod function to find the root x2 which is around 1.2
print("The root at x2 is", ans2)

endTime = time.time() #records the time when the program stops
print("Execution time:", (endTime - startTime)/1000, "seconds") #prints the time in seconds taken for the program to execute
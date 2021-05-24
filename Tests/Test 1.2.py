import math
import time

startTime = time.time() #records the time when the program starts executing

def f(x): #function f(x)
    y = x**5 - 5*x**4 + 5*x**3 + 5*x**2 - 6*x - 1
    return y 

def newtonMethod(x0):#Newton's method for finding roots
    x = x0
    if abs(f(x)) <= 0.000005: #checks the the error is less than 
        return (x) #returns the x value
    return newtonMethod(x - (f(x)/ derivativeCD(x))) #iterates Newton's Method until solution is found

def derivativeCD(x): #calculating the derivative using Central Difference
    return (f(x + 1E-7)- f(x - 1E-7))/(2E-7) #h value of 1E-7 is used

ans1 = newtonMethod(-1) #first root
print(ans1)
ans2 = newtonMethod(-0.1) #second root
print(ans2)

endTime = time.time() #records the time when the program stops
print("Execution time:", endTime - startTime, "seconds") #prints the time in seconds taken for the program to execute
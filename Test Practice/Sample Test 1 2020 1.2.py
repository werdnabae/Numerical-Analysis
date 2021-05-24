import math
import time

def fsinc(x):
    y = math.sin(x)/x
    return y 

def fcos(x):
    y = math.cos(x)
    return y 

def combined(x):
    y = math.sin(x)/x - math.cos(x)
    return y

def newtonMethod(x0, count):#Newton's method for finding roots
    x = x0
    count = count + 1
    if abs(combined(x)) <= 0.000005: #checks the the error is less than 
        return (x, count) #returns the x value
    return newtonMethod(x - (combined(x)/ derivativeCD(x)), count) #iterates Newton's Method until solution is found

def derivativeCD(x): #calculating the derivative using Central Difference
    return (combined(x + 1E-7)- combined(x - 1E-7))/(2E-7) #h value of 1E-6 is used

(ans1, count) = newtonMethod(5, 0)
print(ans1, count)
(ans2, count) = newtonMethod(8, 0)
print(ans2, count)
(ans3, count) = newtonMethod(11, 0)
print(ans3, count)
(ans4, count) = newtonMethod(14, 0)
print(ans4, count)
(ans5, count) = newtonMethod(17, 0)
print(ans5, count)

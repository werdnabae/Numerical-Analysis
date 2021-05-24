import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from random import *

N = np.zeros(10000)
M = np.zeros(1000)
total = 0
for i in range(0, len(N)):
    
    N[i] = random() * 4 - 2
    total = total + N[i]
    if (i + 1) % 10 ==0:      
        M[int((i - 9)/10)] = total
        total = 0
 
G = [-4, -3 , -2, -1, 1, 2, 3, 4]
P = [0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0, len(M)):
    if M[i] > -20 and M[i] < -15:
        P[0] = 1 + P[0]

    if M[i] > -15 and M[i] < -10:
        P[1] = 1 + P[1]

    if M[i] > -10 and M[i] < -5:
        P[2] = 1 + P[2]

    if M[i] > -5 and M[i] < 0:
        P[3] = 1 + P[3]

    if M[i] > 0 and M[i] < 5:
        P[4] = 1 + P[4]

    if M[i] > 5 and M[i] < 10:
        P[5] = 1 + P[5]

    if M[i] > 10 and M[i] < 15:
        P[6] = 1 + P[6]

    if M[i] > 15 and M[i] < 20:
        P[7] = 1 + P[7]

def form(g, A, B):
    return A * np.exp(-B * (g**2))

fit, pcov = curve_fit(form, G, P)
print(fit)
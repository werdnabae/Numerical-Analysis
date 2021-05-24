import matplotlib.pyplot as plt
import math
from math import comb #combinations: (nCk)
import numpy as np

# This code should work for creating any distributions, just change the function
print(math.factorial(5)) 
print(comb(10, 3))

#Binomial Distribution

def binomial(k, n, p):
    return comb(n, k) * (p**k) * ((1 - p)**(n-k))

distributions = []
n = 40
p = 0.5
for i in range(40):
    distributions.append(binomial(i, n, p))
    print(distributions[i])

#Root Mean Squared
disArray = np.array(distributions)
arithMean = np.mean(disArray)
rms = np.sqrt(np.mean(disArray**2))
print(arithMean)
print(rms)

plt.plot(distributions)
plt.show()


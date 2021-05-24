import numpy as np
import matplotlib.pyplot as plt

h = 1E-4
x = np.arange(-1, 1+h , h) 
y = np.zeros(len(x))
for i in range(0, len(x)):
    y[i] = abs(x[i]) - 1

n = len(x)
f = np.fft.fft(y, n)
freq = np.fft.fftfreq(len(f), h)

#plt.plot(x, y)
plt.plot(freq, f.real)
plt.xlim([-5, 5])
plt.show()

"""
N = 100 # number of samplepoints
f_s = 100
x = np.linspace(-1, 1, 2 * f_s) 
y = np.zeros(len(x))
for i in range(0, len(x)):
    y[i] = abs(x[i]) - 1

f = np.fft.fft(y)
freq = np.fft.fftfreq(len(x)) * f_s

plt.plot(freq, np.abs(f))
plt.show()
"""
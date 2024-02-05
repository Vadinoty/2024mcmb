import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def sigmoid(x, a, b, c):
    return c / (1 + np.exp(-a*(x-b)))
x = np.array([1, 2, 3, 4, 5])
y = np.array([0.1, 0.4, 0.5, 0.9, 1.0])

popt, pcov = curve_fit(sigmoid, x, y)
x_fit = np.linspace(1, 5, 100)
y_fit = sigmoid(x_fit, *popt)

plt.scatter(x, y, label='data')
plt.plot(x_fit, y_fit, label='fit', color='r')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

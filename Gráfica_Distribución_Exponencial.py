import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

lam = 1.5
x = np.linspace(0,6,500)
y = expon.pdf(x,scale=1 / lam)

plt.plot(x,y)
plt.title('Distribución Exponencial')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
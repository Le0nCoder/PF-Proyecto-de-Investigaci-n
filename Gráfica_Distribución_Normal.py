import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mu = 170
sigma = 10
x =  np.linspace(130,210,500)
y = norm.pdf(x,loc=mu, scale=sigma)

plt.plot(x,y)
plt.title('Distribución Normal N(170, 10)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
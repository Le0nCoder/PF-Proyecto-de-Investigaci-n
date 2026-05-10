import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

a = 2
b = 8
x = np.linspace(0,10,500)
y = uniform.pdf(x,loc=a,scale = b -a )

plt.plot(x,y)
plt.title('Distribución unforme U(2,8)')
plt.xlabel("x")
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

x = np.linspace(-4,4,500)
for gl in [2,8,30]:
    y = t.pdf(x,df=gl)
    plt.plot(x,y,label = f'gl={gl}')

plt.title('Distribución T-Student')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
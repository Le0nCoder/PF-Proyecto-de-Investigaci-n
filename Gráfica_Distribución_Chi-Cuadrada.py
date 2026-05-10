import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

x = np.linspace(0,20,500)
for gl in [2,5,10]:
    y = chi2.pdf(x,df=gl)
    plt.plot(x,y,label = f'gl={gl}')

plt.title('Distribución Chi-Cuadrada')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
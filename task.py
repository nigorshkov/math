%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 201)
plt.plot(x, np.cos(x))
plt.plot(x, np.cos(5*x))
plt.xlabel('x')
plt.ylabel('y')
plt.axis('tight')
plt.show()
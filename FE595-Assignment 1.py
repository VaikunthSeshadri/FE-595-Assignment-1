
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*np.pi, 0.01)
y = np.sin(x)
z = np.cos(x)
t = np.tan(x)

plt.plot(x, y, x, z, x, t)
plt.xlabel('X-values from 0 to 2 pi')
plt.ylabel('sin(x), cos(x), tan(x)')
plt.legend(['sin(x)', 'cos(x)', 'tan(x)'])
plt.title('Plot of sin(x), cos(x) and tan(x) for one period')
plt.show()


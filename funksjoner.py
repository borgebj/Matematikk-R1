import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

x = np.linspace(-3, 3, 100)
y = f(x)

# style
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
plt.grid()

plt.plot(x, y) # f(x) - vanlig
plt.plot(y, x) # f^-1(x) - invers

# punkt i (2, f(2))
plt.plot(2, f(2), "ro")
plt.show()

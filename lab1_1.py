#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 1, 0.01)
# x = np.arange(-0.5, 2, 0.05)

f1 = lambda x: (2*x)  * (x <= 1) * (x >= 0)
f2 = lambda x: (x**2) * (x <= 1) * (x >= 0) + (x > 1)
f3 = lambda x: (np.sqrt(x * (x >= 0)))

y1 = f1(x)
y2 = f2(x)
y3 = f3(x)

fig, (ax) = plt.subplots(1, 2)
ax[0].plot(x, y1, label='Gęstość prawd.')
ax[0].plot(x, y2, label='Dystrybuanta')
ax[0].plot(x, y3, label='Odwrotna dyst.')
ax[0].set_ylabel('Y')
ax[0].set_xlabel('X')
ax[0].legend()

ax[1].hist(y3, density=True, label="Histogram")
ax[1].plot(x, y1, label='Gęstość prawd.')
ax[1].set_xlabel('Wartość próbki')
ax[1].set_ylabel('Ilość próbek o danej wartości')
ax[1].legend()

plt.show()
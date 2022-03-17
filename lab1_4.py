#!/usr/bin/env python

from cProfile import label
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-1, 1, 0.00001)
x2 = np.arange(-5, 5, 0.00001)

f1 = lambda x: 0.5 * np.power(np.e, -np.abs(x))
f2 = lambda x: 0.5 + 0.5 * (1 - np.power(np.e, -np.abs(x))) * (x >= 0) - 0.5 * (1 - np.power(np.e, -np.abs(x))) * (x < 0)
f3 = lambda x:  -np.log(1 - x) * (x >= 0) + np.log(1 + x) * (x < 0)

y1 = f1(x2)
y2 = f2(x2)
y3 = f3(x2)


fig, (ax) = plt.subplots(1, 2)
ax[0].plot(x2, y1, label='Gęstość prawd.')
ax[0].plot(x2, y2, label='Dystrybuanta')
ax[0].plot(x2, y3, label='Odwrotna dyst.')
ax[0].set_ylabel('Y')
ax[0].set_xlabel('X')
ax[0].legend()

ax[1].hist(y3, density=True, label="Histogram", range=(-5,5), bins=100)
ax[1].plot(x2, y1, label='Gęstość prawd.')
ax[1].set_xlabel('Wartość próbki')
ax[1].set_ylabel('Ilość próbek o danej wartości')
ax[1].legend()

plt.show()
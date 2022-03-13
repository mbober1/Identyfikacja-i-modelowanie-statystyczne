#!/usr/bin/env python

from cProfile import label
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-6, 6, 0.0001)

f1 = lambda x: 0.5 * np.power(np.e, -np.abs(x))
f2 = lambda x: 0.5 * np.power(np.e, -np.abs(x))
f3 = lambda x: -np.log(2*x)

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
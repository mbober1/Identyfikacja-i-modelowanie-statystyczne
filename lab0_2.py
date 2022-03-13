#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt


def generate_numbers(results_count, start_value, c, m):
  a = np.arange(0, results_count)
  y = np.zeros(results_count)

  y[0] = start_value
  
  for i in range(1, results_count):
    tmp = np.multiply(a, np.flip(y))
    y[i] = np.mod(tmp.sum() + c, m)

  return y


start_value = 0.001
results_count = 150
c = 0.01769
m = 1 #zakres

x = np.arange(0, results_count)
y = generate_numbers(results_count, start_value, c, m)

title = "M = " + str(m) + ", C = " + str(c) + ", Start = " + str(start_value)

fig, (ax) = plt.subplots(1, 2)
fig.suptitle(title)
ax[0].plot(x, y, 'o')
ax[0].set_ylabel('Wartość próbki')
ax[0].set_xlabel('Numer próbki')

ax[1].hist(y, density=True, label="Histogram")
ax[1].set_xlabel('Wartość próbki')
ax[1].set_ylabel('Ilość próbek o danej wartości')
ax[1].legend()

plt.show()
#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt


def generate_numbers(results_count, start_value, c, m, k):
  x = np.zeros(1)
  x[0] = start_value
  
  for i in range(1, results_count):
    a = np.arange(i) + 1

    tmp = a * np.flip(x)
    x = np.append(x, np.mod(tmp.sum() +c, m))

  return x


start_value = 0.2137
results_count = 10000
c = 0.01769
m = 1 #zakres
k = 10

x = np.arange(0, results_count)
y = generate_numbers(results_count, start_value, c, m, k)

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
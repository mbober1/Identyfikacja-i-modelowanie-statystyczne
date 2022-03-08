#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt

def generate(x, z):
  tmp = x*z
  return tmp - np.floor(tmp)

def generate_numbers(z, results_count, start_value):
  x = np.arange(0, results_count)
  y = np.zeros(results_count)

  y[0] = start_value

  for i in range(1, results_count):
    y[i] = generate(y[i-1], z)

  return x, y




z = 69
start_value = 0.01
results_count = 20000

x, y = generate_numbers(z, results_count, start_value)

fig, (ax1) = plt.subplots(1, 1)
# fig, (ax1, ax2) = plt.subplots(2, 1)

title = "Z = " + str(z) + ", X = " + str(start_value)
fig.suptitle(title)

# ax1.plot(x, y, 'o')
# ax1.set_ylabel('Wartość próbki')
# ax1.set_xlabel('Numer próbki')

ax1.hist(y)
ax1.set_xlabel('Wartość próbki')
ax1.set_ylabel('Ilość próbek o danej wartości')

plt.show()
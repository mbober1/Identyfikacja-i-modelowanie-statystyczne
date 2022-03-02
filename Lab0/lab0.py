#!/usr/bin/env python

import numpy as np
from math import floor
from matplotlib import pyplot as plt

def generate(x, z):
  tmp = x*z
  return tmp - floor(tmp)

def generate_numbers(seed, results_count):
  x = np.arange(0, results_count)
  y = np.zeros(results_count)

  y[0] = 0.01

  for i in range(1, results_count):
    y[i] = generate(y[i-1], seed)

  return x, y


seed = 69
results_count = 1000

x, y = generate_numbers(seed, results_count)

fig, (ax1, ax2) = plt.subplots(2, 1)
# fig.suptitle('A tale of 2 subplots')

ax1.plot(x, y, 'o')
# ax1.set_ylabel('Damped oscillation')

ax2.hist(y)
# ax2.set_xlabel('Wartość')
# ax2.set_ylabel('Histogram')

plt.show()
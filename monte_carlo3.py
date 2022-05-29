#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt
  

def find_pi(samples):
  circle_points = 0
  rand_x = np.random.uniform(-1, 1, samples)
  rand_y = np.random.uniform(-1, 1, samples)
  origin_dist = np.power(rand_x, 2) + np.power(rand_y, 2)

  for point in origin_dist:
    if point <= 1:
      circle_points += 1

  pi = 4 * circle_points / samples
  return pi

count = 1000000
results = []
samples = np.arange(1000, count, int(count/100))

f = lambda samples: find_pi(samples)

for i in samples:
  results.append(f(i))


x = np.linspace(0, count)

fig, (ax) = plt.subplots(1, 1)
ax.plot(samples, results, 'o')
ax.plot(x, x*0 + np.pi, linestyle='dashed')
ax.set_ylabel('Y')
ax.set_xlabel('X')
ax.legend()

plt.show()
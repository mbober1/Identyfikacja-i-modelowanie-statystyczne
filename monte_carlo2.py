#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt
  
count = 2000
circle_points_x = []
circle_points_y = []
not_circle_points_x = []
not_circle_points_y = []

rand_x = np.random.uniform(-1, 1, count)
rand_y = np.random.uniform(-1, 1, count)
origin_dist = rand_x**2 + rand_y**2

for i in range(origin_dist.size):
  if origin_dist[i] <= 1:
    circle_points_x.append(rand_x[i])
    circle_points_y.append(rand_y[i])
  else:
    not_circle_points_x.append(rand_x[i])
    not_circle_points_y.append(rand_y[i])


fig, (ax) = plt.subplots(1, 1)
ax.plot(circle_points_x, circle_points_y, 'o')
ax.plot(not_circle_points_x, not_circle_points_y, 'o')
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()

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


samples = 50000000
pi = find_pi(samples)
print("Samples=", samples)
print("Final estimation of Pi:", pi)  
print("Real Pi value:", np.pi)  
print("Error", np.abs(pi - np.pi))  
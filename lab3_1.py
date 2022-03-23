#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt

count = 100000

mu = 0
sigma = 5

T = sigma * np.random.randn(count) + mu

estimator1 = np.sum(T) / count
estimator2 = np.sum(np.power(T - estimator1, 2)) / count
estimator3 = np.sum(np.power(T - estimator1, 2)) / (count - 1)

print(estimator1)
print(estimator2)
print(estimator3)
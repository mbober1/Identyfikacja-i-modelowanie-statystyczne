#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt

count = 10000000

T = np.random.standard_cauchy(count)

estimator1 = np.sum(T) / count
estimator2 = np.sum(np.power(T - estimator1, 2)) / count
estimator3 = np.sum(np.power(T - estimator1, 2)) / (count - 1)

print(estimator1)
print(estimator2)
print(estimator3)
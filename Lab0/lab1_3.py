#!/usr/bin/env python

import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 1, 0.001)

f =  lambda x:  (np.power(np.e, -x)) * (x >= 0)
f2 = lambda x: -(np.power(np.e, -x)) * (x >= 0)
f3 = lambda x: -(np.log(1 - x))    * (x >= 0)

y = f(x)
y2 = f2(x)
y3 = f3(x)

fig, (ax1) = plt.subplots(1, 1)
# # fig, (ax1, ax2) = plt.subplots(2, 1)

# title = "Z = " + str(z) + ", X = " + str(start_value)
# fig.suptitle(title)

# ax1.plot(x, y)
# ax1.plot(x, y2)
# ax1.plot(x, y3)
# # ax1.set_ylabel('Wartość próbki')
# # ax1.set_xlabel('Numer próbki')

ax1.hist(y3)
# ax1.set_xlabel('Wartość próbki')
# ax1.set_ylabel('Ilość próbek o danej wartości')

plt.show()
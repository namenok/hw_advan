import random
import numpy as np

import matplotlib.pyplot as plt
from random import randint

mu, sigma = 0, 0.1 # mean and standard deviation
digits = np.random.normal(mu, sigma, 1000)

plt.hist(digits, bins=25, density=True, alpha=0.6, color='b')

plt.show()
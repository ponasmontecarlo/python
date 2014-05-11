from functions import *
import numpy as np
import itertools
import math
import scipy
from scipy.stats import chi
import scipy.integrate
import matplotlib.pyplot as plt
import time

#### PARAMETERS ####
upperOmegaBound = 10
nOmegas = 200
nu = 5
M = 50
d = 4
n = 5
rho = 0.1
mu = [0, 0, 0, 0]
sigma = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
estimate = pV
region = orthant
regionNumber = 1
#####################

# import pandas as pd
#
# A2 = pd.read_csv('C:/Users/Adomas/Dropbox/Bakalaurinis/vektoriai/A2.csv', sep=" ", header=None)

# a = []
# [a.append(studentProb(upperOmegaBound, nOmegas, nu, M, estimate, d, n, mu, sigma, region, regionNumber)) for _ in itertools.repeat(None, 1000)]
# print(np.mean(a))

tic = time.clock()
print(studentProb(upperOmegaBound, nOmegas, nu, M, estimate, d, mu, sigma, region, regionNumber))
toc = time.clock()
print('Elapsed time = ', (toc - tic), 'seconds')
from functions import *
import numpy as np
import itertools
import math
import scipy
from scipy.stats import chi
import scipy.integrate
import time

#### PARAMETERS ####
upperOmegaBound = 5
nOmegas = 100
nu = 5
M = 1000
d = 3
rho = 0.1
#mu = [0, 0, 0, 0]
mu = [0, 0, 0]
#sigma = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
sigma = identity
estimate = pVantithetic
region = orthant
regionNumber = 1
#####################

tic = time.clock()
print('Estimated probability=', studentProb(upperOmegaBound, nOmegas, nu, M, estimate, d, mu, sigma, rho, region, regionNumber))
toc = time.clock()
elapsed = (toc - tic)
print('Elapsed time = ', elapsed, 'seconds')
print('Predicted all simulations time = ', 3000*10000*elapsed, 'seconds')
print('or', 3000*10000*elapsed/60, 'minutes')
print('or', 3000*10000*elapsed/3600, 'hours')
print('or', 3000*10000*elapsed/(24*3600), 'days')
print('or', 3000*10000*elapsed/(365*24*3600), 'years')
print('SAY WHAAAT???')
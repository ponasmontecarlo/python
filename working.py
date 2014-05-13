from pip.util import Inf
from functions import *
import numpy as np
import itertools
import math
import scipy
from scipy.stats import chi
import time
from scipy.integrate import quad
from scipy import integrate

#### PARAMETERS ####

nu = 5
M = 500
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
print('Estimated probability=', studentProb(0.1, 5.4, 0.15, nu,  M, Crude, d, mu, sigma, rho, region, regionNumber))
toc = time.clock()
elapsed = (toc - tic)
print('Elapsed time = ', elapsed, 'seconds')
print('Estimate time of 500 simulations = ', 500*elapsed/60, 'minutes')
tic = time.clock()
print('Estimated probability=', studentProb(0.1, 5.4, 0.15, nu,  M, antithetic, d, mu, sigma, rho, region, regionNumber))
toc = time.clock()
elapsed = (toc - tic)
print('Elapsed time = ', elapsed, 'seconds')
print('Estimate time of 500 simulations = ', 500*elapsed/60, 'minutes')
tic = time.clock()
print('Estimated probability=', studentProb(0.1, 5.4, 0.15, nu,  M, pV, d, mu, sigma, rho, region, regionNumber))
toc = time.clock()
elapsed = (toc - tic)
print('Elapsed time = ', elapsed, 'seconds')
print('Estimate time of 500 simulations = ', 500*elapsed/3600, 'hours')
tic = time.clock()
print('Estimated probability=', studentProb(0.1, 5.4, 0.15, nu,  M, pVantithetic, d, mu, sigma, rho, region, regionNumber))
toc = time.clock()
elapsed = (toc - tic)
print('Elapsed time = ', elapsed, 'seconds')
print('Estimate time of 500 simulations = ', 500*elapsed/3600, 'hours')

# print('Predicted all simulations time = ', 3000*10000*elapsed, 'seconds')
# print('or', 3000*10000*elapsed/60, 'minutes')
# print('or', 3000*10000*elapsed/3600, 'hours')
# print('or', 3000*10000*elapsed/(24*3600), 'days')
# print('or', 3000*10000*elapsed/(365*24*3600), 'years')
# print('SAY WHAAAT???')

# # TEST
#
# nu = 5
# criteria = 0.0001
# lower = determineLowerBound(nu, criteria)
# print('Lower:', lower)
# upper = determineUpperBound(nu, lower, criteria)
# print('Upper:', upper)
# step = determineStep(nu, lower, upper, 0.5, criteria)
# print('Step size:', step)
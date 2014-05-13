from functions import *
import time
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
# parinkti parametrus
nu = 5
M = 500
rho = 0.1
sigma = identity
estimate = pV
region = orthant
regionNumber = 1
simulations = 500
criteria = 0.0001
initStep = 0.3


dropboxDestination = 'C:/Users/Adomas/Dropbox/Bakalaurinis/results/' # cia nurodot savo dropboxo results folderi

# SHOULD BE CHECKED BY PERSON
lower = determineLowerBound(nu, criteria)
upper = determineUpperBound(nu, lower, criteria)
step = determineStep(nu, lower, upper, initStep, criteria)

print('Lower bound:', lower)
print('Upper bound:', upper)
print('Step size:', step)

# first

d = 2
mu = [0, 0]

fileName = "%s_dim%s_df%s_%s_%s%s" % (estimate.__name__, d, nu, sigma.__name__, region.__name__, regionNumber)
resultsFile = open(str(dropboxDestination)+str(fileName)+'.txt', 'a')

for _ in itertools.repeat(None, simulations):
    estimated = studentProb(lower, upper, step, nu, M, estimate, d, mu, sigma, rho, region, regionNumber)
    resultsFile.write("%s\n" % str(estimated))

resultsFile.close()

# second

d = 3
mu = [0, 0, 0]

fileName = "%s_dim%s_df%s_%s_%s%s" % (estimate.__name__, d, nu, sigma.__name__, region.__name__, regionNumber)
resultsFile = open(str(dropboxDestination)+str(fileName)+'.txt', 'a')

for _ in itertools.repeat(None, simulations):
    estimated = studentProb(lower, upper, step, nu, M, estimate, d, mu, sigma, rho, region, regionNumber)
    resultsFile.write("%s\n" % str(estimated))

resultsFile.close()
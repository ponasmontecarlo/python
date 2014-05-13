from pip.util import Inf
from functions import *
import numpy as np
import itertools
import math
import scipy
from scipy.stats import chi
import scipy.integrate
import time
from scipy.integrate import quad
import scipy.integrate
import matplotlib.pyplot as plt
from pylab import *
from scipy import integrate

#### PARAMETERS ####
upperOmegaBound = 5
nOmegas = 50
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

# tic = time.clock()
# print('Estimated probability=', studentProb(upperOmegaBound, nOmegas, nu, M, estimate, d, mu, sigma, rho, region, regionNumber))
# toc = time.clock()
# elapsed = (toc - tic)
# print('Elapsed time = ', elapsed, 'seconds')
# print('Predicted all simulations time = ', 3000*10000*elapsed, 'seconds')
# print('or', 3000*10000*elapsed/60, 'minutes')
# print('or', 3000*10000*elapsed/3600, 'hours')
# print('or', 3000*10000*elapsed/(24*3600), 'days')
# print('or', 3000*10000*elapsed/(365*24*3600), 'years')
# print('SAY WHAAAT???')

# function inside integral
def innerFunction(omega, nu):
    return (omega ** (nu - 1))*(math.exp(-((omega ** 2)/2)))

# give nu and criteria how much you allow to be near zero and lowerbound will be given
def determineLowerBound(nu, criteria):
    testPoints = np.arange(0.0, 5.0, 0.1)
    testResults = []
    [testResults.append(innerFunction(testPoints[i], nu)) for i in range(len(testPoints))]
    return testPoints[np.max(np.where(np.array(testResults) < criteria))]

# give nu and lower from determinelowerbound and criteria, upperbound will be given
def determineUpperBound(nu, lower, criteria):
    testPoints = np.arange(lower, 20.0, 0.1)
    testResults = []
    [testResults.append(quad(innerFunction, testPoints[i], np.inf, args=nu)[0]) for i in range(len(testPoints))]
    return testPoints[np.min(np.where(np.array(testResults) < criteria))]

# give evything, optimal step will be given
def determineStep(nu, lower, upper, initStep, criteria):
    last = 0
    while True:
        testPoints = np.arange(lower, upper, initStep)
        testResults = []
        [testResults.append(innerFunction(testPoints[i], nu)) for i in range(len(testPoints))]
        if math.fabs(integrate.simps(testResults, testPoints) - last) < criteria:
            break
        else:
            last = integrate.simps(testResults, testPoints)
            initStep -= 0.05
    return initStep

# TEST

nu = 6
criteria = 0.0001
lower = determineLowerBound(nu, criteria)
print('Lower:', lower)
upper = determineUpperBound(nu, lower, criteria)
print('Upper:', upper)
step = determineStep(nu, lower, upper, 0.5, criteria)
print('Step size:', step)
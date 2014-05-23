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
nu = 7
M = 500
rho = 0.1
sigma = oneFactor
estimate = Crude
region = elipsoid
regionNumber = 2
simulations = 200
criteria = 0.0001
initStep = 0.3


dropboxDestination = 'C:/Users/Adomas/Dropbox/Bakalaurinis/results/' # cia nurodot savo dropboxo results folderi

# SHOULD BE CHECKED BY PERSON
# lower = determineLowerBound(nu, criteria)
# upper = determineUpperBound(nu, lower, criteria)
# step = determineStep(nu, lower, upper, initStep, criteria)
#
# print('Lower bound:', lower)
# print('Upper bound:', upper)
# print('Step size:', step)


# lower = 0.1
# upper = 5.4
# step = 0.15

# nu = 0.5
# lower=0.001
# upper=3.801
# step = 0.11875

# nu = 2
# lower = 0.015
# upper = 4.315
# step = 0.2



##### PIRMAS

region = orthant
regionNumber = 1
d = 5
mu = np.repeat(0,5)
sigma = identity

nu = 7
lower = 0.2
upper = 6.1
step = 0.2

fileName = "%s_dim%s_df%s_%s_%s%s" % (estimate.__name__, d, nu, sigma.__name__, region.__name__, regionNumber)
print(fileName)
resultsFile = open(str(dropboxDestination)+str(fileName)+'.txt', 'a')

for _ in itertools.repeat(None, simulations):
    estimated = studentProb(lower, upper, step, nu, M, estimate, d, mu, sigma, rho, region, regionNumber)
    resultsFile.write("%s\n" % str(estimated))

resultsFile.close()


# ####### ANTRAS
#
# region = orthant
# regionNumber = 1
# d = 3
# mu = [0, 0, 0]
#
# nu = 5
# lower = 0.1
# upper = 5.4
# step = 0.15
# #
# region = orthant
# regionNumber = 1
# sigma = identity
#
# fileName = "%s_dim%s_df%s_%s_%s%s" % (estimate.__name__, d, nu, sigma.__name__, region.__name__, regionNumber)
# print(fileName)
# resultsFile = open(str(dropboxDestination)+str(fileName)+'.txt', 'a')
#
# for _ in itertools.repeat(None, simulations):
#     estimated = studentProb(lower, upper, step, nu, M, estimate, d, mu, sigma, rho, region, regionNumber)
#     resultsFile.write("%s\n" % str(estimated))
#
# resultsFile.close()
#
#
# region = elipsoid
# regionNumber = 2
# sigma = identity
#
# fileName = "%s_dim%s_df%s_%s_%s%s" % (estimate.__name__, d, nu, sigma.__name__, region.__name__, regionNumber)
# print(fileName)
# resultsFile = open(str(dropboxDestination)+str(fileName)+'.txt', 'a')
#
# for _ in itertools.repeat(None, simulations):
#     estimated = studentProb(lower, upper, step, nu, M, estimate, d, mu, sigma, rho, region, regionNumber)
#     resultsFile.write("%s\n" % str(estimated))
#
# resultsFile.close()
#
#
# #
# #
# # ####### TRECIAS
# #
# #
# # region = elipsoid
# # regionNumber = 2
# # d = 3
# # mu = [0, 0, 0]
# #
# # nu = 5
# # lower = 0.1
# # upper = 5.4
# # step = 0.15
# #
# # fileName = "%s_dim%s_df%s_%s_%s%s" % (estimate.__name__, d, nu, sigma.__name__, region.__name__, regionNumber)
# # print(fileName)
# # resultsFile = open(str(dropboxDestination)+str(fileName)+'.txt', 'a')
# #
# # for _ in itertools.repeat(None, simulations):
# #     estimated = studentProb(lower, upper, step, nu, M, estimate, d, mu, sigma, rho, region, regionNumber)
# #     resultsFile.write("%s\n" % str(estimated))
# #
# # resultsFile.close()
# #
# # ###### Ketvirtas
# #
# #
#
# nu = 5
# lower = 0.1
# upper = 5.4
# step = 0.15
#
# region = orthant
# regionNumber = 1
# sigma = oneFactor
#
# fileName = "%s_dim%s_df%s_%s_%s%s" % (estimate.__name__, d, nu, sigma.__name__, region.__name__, regionNumber)
# print(fileName)
# resultsFile = open(str(dropboxDestination)+str(fileName)+'.txt', 'a')
#
# for _ in itertools.repeat(None, simulations):
#     estimated = studentProb(lower, upper, step, nu, M, estimate, d, mu, sigma, rho, region, regionNumber)
#     resultsFile.write("%s\n" % str(estimated))
#
# resultsFile.close()
#
# region = elipsoid
# regionNumber = 2
# sigma = oneFactor
#
# fileName = "%s_dim%s_df%s_%s_%s%s" % (estimate.__name__, d, nu, sigma.__name__, region.__name__, regionNumber)
# print(fileName)
# resultsFile = open(str(dropboxDestination)+str(fileName)+'.txt', 'a')
#
# for _ in itertools.repeat(None, simulations):
#     estimated = studentProb(lower, upper, step, nu, M, estimate, d, mu, sigma, rho, region, regionNumber)
#     resultsFile.write("%s\n" % str(estimated))
#
# resultsFile.close()
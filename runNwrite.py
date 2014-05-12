from functions import *
import time

#### PARAMETERS ####
# parinkti parametrus
upperOmegaBound = 5
nOmegas = 100
nu = 5
M = 500
rho = 0.1
sigma = identity
estimate = pVantithetic
region = orthant
regionNumber = 1
simulations = 2

dropboxDestination = '/home/adomas/Dropbox/Bakalaurinis/results/' # cia nurodot savo dropboxo results folderi
# first

d = 2
mu = [0, 0]



fileName = "estimate_%s_dim%s_df%s_%s_%s%s" % (estimate.__name__, d, nu, sigma.__name__, region.__name__, regionNumber)
resultsFile = open(str(dropboxDestination)+str(fileName)+'.txt', 'a')

for _ in itertools.repeat(None, simulations):
    estimated = studentProb(upperOmegaBound, nOmegas, nu, M, estimate, d, mu, sigma, rho, region, regionNumber)
    resultsFile.write("%s\n" % str(estimated))

resultsFile.close()

# second

d = 3
mu = [0, 0, 0]

fileName = "estimate_%s_dim%s_df%s_%s_%s%s" % (estimate.__name__, d, nu, sigma.__name__, region.__name__, regionNumber)
resultsFile = open(str(dropboxDestination)+str(fileName)+'.txt', 'a')

for _ in itertools.repeat(None, simulations):
    estimated = studentProb(upperOmegaBound, nOmegas, nu, M, estimate, d, mu, sigma, rho, region, regionNumber)
    resultsFile.write("%s\n" % str(estimated))

resultsFile.close()

# third

d = 4
mu = [0, 0, 0, 0]

fileName = "estimate_%s_dim%s_df%s_%s_%s%s" % (estimate.__name__, d, nu, sigma.__name__, region.__name__, regionNumber)
resultsFile = open(str(dropboxDestination)+str(fileName)+'.txt', 'a')

for _ in itertools.repeat(None, simulations):
    estimated = studentProb(upperOmegaBound, nOmegas, nu, M, estimate, d, mu, sigma, rho, region, regionNumber)
    resultsFile.write("%s\n" % str(estimated))

resultsFile.close()

# fourth

d = 5
mu = [0, 0, 0, 0, 0]

fileName = "estimate_%s_dim%s_df%s_%s_%s%s" % (estimate.__name__, d, nu, sigma.__name__, region.__name__, regionNumber)
resultsFile = open(str(dropboxDestination)+str(fileName)+'.txt', 'a')

for _ in itertools.repeat(None, simulations):
    estimated = studentProb(upperOmegaBound, nOmegas, nu, M, estimate, d, mu, sigma, rho, region, regionNumber)
    resultsFile.write("%s\n" % str(estimated))

resultsFile.close()
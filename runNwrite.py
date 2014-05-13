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
estimate = pV
region = orthant
regionNumber = 1
simulations = 500

dropboxDestination = 'C:/Users/Adomas/Dropbox/Bakalaurinis/results/' # cia nurodot savo dropboxo results folderi
# first

d = 3
mu = [0, 0, 0]


fileName = "estimate_%s_dim%s_df%s_%s_%s%s" % (estimate.__name__, d, nu, sigma.__name__, region.__name__, regionNumber)
resultsFile = open(str(dropboxDestination)+str(fileName)+'.txt', 'a')

for _ in itertools.repeat(None, simulations):
    estimated = studentProb(upperOmegaBound, nOmegas, nu, M, estimate, d, mu, sigma, rho, region, regionNumber)
    resultsFile.write("%s\n" % str(estimated))

resultsFile.close()

# second


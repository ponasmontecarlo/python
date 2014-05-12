from functions import *
import time

#### PARAMETERS ####
# parinkti parametrus
upperOmegaBound = 10
nOmegas = 200
nu = 5
M = 1000
d = 2
rho = 0.1
mu = [0, 0]
sigma = [[1, 0], [0, 1]]
estimate = Crude
region = orthant
regionNumber = 1
simulations = 50

dropboxDestination = '/home/adomas/Dropbox/Bakalaurinis/results/' # cia nurodot savo dropboxo results folderi
fileName = 'adomas_results_crude_5d' # parasot kaip norit, jog vadintusi

#####################
# viska atlieka pats
resultsFile = open(str(dropboxDestination)+str(fileName)+'.txt', 'w')
resultsFile.write("Estimate: %s\n" % estimate.__name__)
resultsFile.write("Degrees of freedom: %s\n" % nu)
resultsFile.write("mu: %s, sigma: %s \n" % (mu, sigma))
resultsFile.write("Inside runs: %s, simulations %s\n" % (M, simulations))
resultsFile.write("Region: %s %s\n" % (region.__name__, regionNumber))
resultsFile.write("Dimension: %s\n" % d)
resultsFile.write("Integration upper bound: %s, number of steps %s\n" % (upperOmegaBound, nOmegas))
tic = time.clock()
resultsFile.write("\n")

for _ in itertools.repeat(None, simulations):
    estimated = studentProb(upperOmegaBound, nOmegas, nu, M, estimate, d, mu, sigma, region, regionNumber)
    resultsFile.write("%s\n" % str(estimated))

toc = time.clock()
resultsFile.write("Elapsed time: %s seconds\n" % (toc - tic))
resultsFile.close()
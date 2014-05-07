##########
# IMPORTS
##########

from functions import elipsoid, orthant, rectangular, pV, Crude, antithetic, pVantithetic
import numpy as np
import itertools

#############
# PARAMETERS
#############

d = 3  # dimension
n = 5  # number of v's which should be chosen later
rho = 0.1  # rho for cov matrices
mu = [0, 0, 0]  # means vector
sigma = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]  # cov matrix which should be constructed later
insideRuns = 100  # number of runs when estimating
simulations = 1000  # number of estimations
region = elipsoid  # region in which we estimate
regionSet = 1  # region code by article


#############
# SIMULATIONS
#############

# Crude estimate
crude = []
[crude.append(Crude(insideRuns, mu, sigma, region, regionSet)) for _ in itertools.repeat(None, simulations)]
varCrude = np.var(crude)

# AT estimate
at = []
[at.append(antithetic(insideRuns, mu, sigma, region, regionSet)) for _ in itertools.repeat(None, simulations)]
varAT = np.var(at)
print('Antithetic variates estimate variance ratio on ', region.__name__, 'set', regionSet, 'is', varCrude/varAT)

# pV estimate
pv = []
[pv.append(pV(insideRuns, d, n, mu, sigma, region, regionSet)) for _ in itertools.repeat(None, simulations)]
varpv = np.var(pv)
print('pV estimate variance ratio on ', region.__name__, 'set', regionSet, 'is', varCrude/varpv)

# pV AT estimate
pvAT = []
[pvAT.append(pVantithetic(insideRuns, d, n, mu, sigma, region, regionSet)) for _ in itertools.repeat(None, simulations)]
varpvAT = np.var(pvAT)
print('pV antithetic variates estimate variance ratio on', region.__name__, 'set', regionSet,'is', varCrude/varpvAT)
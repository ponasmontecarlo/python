from normalUniFunc import oneFactor, covAR, elipsoid,orthant,rectangular, pV, multiNormalAT, radius, orthoT, unitVectors, multiNormalCrude, multiNormalAT, pVAT
import numpy as np
import itertools
import math


d = 3
n = 5
rho = 0.1
t = [0.5, 0.5, 0.5]
mu = [0, 0, 0]
sigma = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

insideRuns = 100
simulations = 1000
region = elipsoid
regionSet = 1

crude = []
[crude.append(multiNormalCrude(insideRuns, mu, sigma, region, regionSet)) for _ in itertools.repeat(None, simulations)]
varCrude = np.var(crude)

at = []
[at.append(multiNormalAT(insideRuns, mu, sigma, region, regionSet)) for _ in itertools.repeat(None, simulations)]
varAT = np.var(at)
print('Antithetic variates estimate variance ratio on ', region.__name__, 'set', regionSet, 'is', varCrude/varAT)

pv = []
[pv.append(pV(insideRuns, d, n, mu, sigma, region, regionSet)) for _ in itertools.repeat(None, simulations)]
varpv = np.var(pv)
print('pV estimate variance ratio on ', region.__name__, 'set', regionSet, 'is', varCrude/varpv)

pvAT = []
[pvAT.append(pVAT(insideRuns, d, n, mu, sigma, region, regionSet)) for _ in itertools.repeat(None, simulations)]
varpvAT = np.var(pvAT)
print('pV antithetic variates estimate variance ratio on', region.__name__, 'set', regionSet,'is', varCrude/varpvAT)
from normalUniFunc import multiNormalCrude, multiNormalAT, orthoT, unitVectors, radius, pV, pVAT, oneFactor, covAR
import numpy as np
import math
import random
import scipy.stats
import scipy
import time

"PARAMETRAI"

d = 3
n = 5
rho = 0.1
t = [0.5, 0.5, 0.5]
mu = [0, 0, 0]
sigma = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

"ESTIMATES"

#Crude estimate
tic = time.clock()
print('Crude = ',multiNormalCrude(50000, t, mu, sigma))
toc = time.clock()
print('Crude time = ',(toc - tic))

#AT estimate
tic = time.clock()
print('AT = ',multiNormalAT(50000, t, mu, sigma))
toc = time.clock()
print('AT time = ',(toc - tic))

#pV estimate
tic = time.clock()
print('pV = ', pV(50000, d, n, t, mu, sigma))
toc = time.clock()
print('pV time = ', (toc - tic))

#pV AT estimate
tic = time.clock()
print('pV AT =', pVAT(25000, d, n, t, mu, sigma))
toc = time.clock()
print('pV AT time = ', (toc - tic))

" Covariance matrices "

#One factor
print(oneFactor(n,rho))
#AR1
print(covAR(n, rho))
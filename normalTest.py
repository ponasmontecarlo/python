from normalUniFunc import multiNormalCrude, multiNormalAT, orthoT, unitVectors, radius, pV, pVAT
import numpy as np
import math
import random
import scipy.stats
import scipy

"PARAMETRAI"

d = 3
n = 5
t = [0.5, 0.5, 0.5]
mu = [0, 0, 0]
sigma = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

"ESTIMATES"

print('Crude = ',multiNormalCrude(10000, t, mu, sigma))
print('AT = ',multiNormalAT(10000, t, mu, sigma))
print('pV = ', pV(10000, d, n, t, mu, sigma))
print('pV AT =', pVAT(10000, d, n, t, mu, sigma))


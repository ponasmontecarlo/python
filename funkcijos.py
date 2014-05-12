import numpy as np, scipy, math, itertools
from scipy.stats import chi
import numpy as np, scipy, math, itertools
from scipy.stats import chi
from functions import *


def studentProb2(upperOmegaBound, nOmegas, nu, M, estimate, d, n, mu, sigma, region, regionNumber):
    omegaX = np.linspace(0.00001, upperOmegaBound, nOmegas)  # points on X axis for integration approximation
    step = upperOmegaBound/nOmegas  # increase of each step

    normalProbabilities = []
    [normalProbabilities.append(estimate(M, d, n, mu, sigma, region, regionNumber, nu, omegaX[i])) for i in range(0, len(omegaX))]

    approxBlocks = []
    [approxBlocks.append(step*(normalProbabilities[i-1]+4*normalProbabilities[i]+normalProbabilities[i+1])/3*approxFunction(nu, omegaX[i])) for i in range(0, len(omegaX))]
    approx = sum(approxBlocks)

    multiplier = (2 ** (1 - (nu/2)))/(math.gamma(nu/2))
    return multiplier*approx
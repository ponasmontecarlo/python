from functions import *
import numpy as np
import itertools
import math
import scipy
from scipy.stats import chi
import scipy.integrate
import matplotlib.pyplot as plt

#### PARAMETERS ####
upperOmegaBound = 10
nOmegas = 200
nu = 5
M = 1000
d = 3
n = 5
rho = 0.1
mu = [0, 0, 0]
sigma = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
estimate = Crude
region = orthant
regionNumber = 3
#####################

#print(studentProb(upperOmegaBound, nOmegas, nu, M, estimate, d, n, mu, sigma, region, regionNumber))
print(np.linspace(0.00001, upperOmegaBound, nOmegas))
# r = np.random.multivariate_normal(mu, sigma, M)
# omega = 0.1
# for x in r:
#     if region((math.sqrt(nu)/omega)*x, regionNumber):
#         d += 1
# print(d)
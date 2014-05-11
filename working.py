from functions import *
import numpy as np
import itertools
import math
import scipy
from scipy.stats import chi
import scipy.integrate
import matplotlib.pyplot as plt


upperOmegaBound = 10
nOmegas = 200
nu = 5
M = 1000
d = 3
n = 5
rho = 0.1
mu = [0, 0, 0]
sigma = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
#
# T = orthoT(d)
# v = unitVectors(d, n)
# u = []
# [u.append(np.dot(T, v[j])) for j in range(n)]
# a = np.array(u[0]).reshape(3,1)
# print(a[2])
# print(scipy.stats.chi.cdf(a[0], 3))
# print(scipy.stats.chi.cdf(a[1], 3))
# print(scipy.stats.chi.cdf(a[2], 3))

#print(studentCrude(10000, mu, sigma, orthant, 1, 5, 100, 1000))

estimate = pV
region = orthant
set = 1
print(studentProb(upperOmegaBound, nOmegas, nu, M, estimate, d, n, mu, sigma, region, set))
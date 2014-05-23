from functions import *
import time
import pandas as pd
import numpy as np


# df = pd.DataFrame(columns=['Crude', 'Antithetic', 'pV', 'pVantithetic'], index=['2', '3', '5'])
# df.fillna(0)

#####

# Parametrai visiems
lower = 0.2
upper = 6.1
step = 0.2
nu = 7
M = 500
rho = 0.1
dim = np.array([2, 3, 5])

# Crude
crude = []
estimate = Crude

for d in dim:
    start_time = time.clock()
    mu = np.repeat(0, d)
    identOrthant = [studentProb(lower, upper, step, nu, M, estimate, d, mu, identity, rho, orthant, 1) for _ in range(2)]
    identElipsoid = [studentProb(lower, upper, step, nu, M, estimate, d, mu, identity, rho, elipsoid, 2) for _ in range(2)]
    oneFacOrthant = [studentProb(lower, upper, step, nu, M, estimate, d, mu, oneFactor, rho, orthant, 1) for _ in range(2)]
    oneFacElipsoid = [studentProb(lower, upper, step, nu, M, estimate, d, mu, oneFactor, rho, elipsoid, 2) for _ in range(2)]
    timeSpent = time.clock() - start_time
    crude.append(timeSpent/8)

# antithetic
anti = []
estimate = antithetic

for d in dim:
    start_time = time.clock()
    mu = np.repeat(0, d)
    identOrthant = [studentProb(lower, upper, step, nu, M, estimate, d, mu, identity, rho, orthant, 1) for _ in range(2)]
    identElipsoid = [studentProb(lower, upper, step, nu, M, estimate, d, mu, identity, rho, elipsoid, 2) for _ in range(2)]
    oneFacOrthant = [studentProb(lower, upper, step, nu, M, estimate, d, mu, oneFactor, rho, orthant, 1) for _ in range(2)]
    oneFacElipsoid = [studentProb(lower, upper, step, nu, M, estimate, d, mu, oneFactor, rho, elipsoid, 2) for _ in range(2)]
    timeSpent = time.clock() - start_time
    anti.append(timeSpent/8)

# pV
pv = []
estimate = pV

for d in dim:
    start_time = time.clock()
    mu = np.repeat(0, d)
    identOrthant = [studentProb(lower, upper, step, nu, M, estimate, d, mu, identity, rho, orthant, 1) for _ in range(2)]
    identElipsoid = [studentProb(lower, upper, step, nu, M, estimate, d, mu, identity, rho, elipsoid, 2) for _ in range(2)]
    oneFacOrthant = [studentProb(lower, upper, step, nu, M, estimate, d, mu, oneFactor, rho, orthant, 1) for _ in range(2)]
    oneFacElipsoid = [studentProb(lower, upper, step, nu, M, estimate, d, mu, oneFactor, rho, elipsoid, 2) for _ in range(2)]
    timeSpent = time.clock() - start_time
    pv.append(timeSpent/8)

# pVanti
pvanti = []
estimate = pVantithetic

for d in dim:
    start_time = time.clock()
    mu = np.repeat(0, d)
    identOrthant = [studentProb(lower, upper, step, nu, M, estimate, d, mu, identity, rho, orthant, 1) for _ in range(2)]
    identElipsoid = [studentProb(lower, upper, step, nu, M, estimate, d, mu, identity, rho, elipsoid, 2) for _ in range(2)]
    oneFacOrthant = [studentProb(lower, upper, step, nu, M, estimate, d, mu, oneFactor, rho, orthant, 1) for _ in range(2)]
    oneFacElipsoid = [studentProb(lower, upper, step, nu, M, estimate, d, mu, oneFactor, rho, elipsoid, 2) for _ in range(2)]
    timeSpent = time.clock() - start_time
    pvanti.append(timeSpent/8)

final = np.matrix([crude, anti, pv, pvanti])
df = pd.DataFrame(final.T, columns=['Crude', 'Antithetic', 'pV', 'pVantithetic'], index=['2', '3', '5'])
print(df)
print(df.to_latex())

m = np.matrix([[0.450, 0.458, 0.451], [1.286, 1.367, 1.327], [25.074, 30.041, 57.134], [27.479, 38.159, 79.667]])
d = pd.DataFrame((8000/3600)*m.T, columns=['Crude', 'Antithetic', 'pV', 'pVantithetic'], index=['2', '3', '5'])


pvantinew = []
estimate = pVantitheticNew

for d in dim:
    start_time = time.clock()
    mu = np.repeat(0, d)
    identOrthant = [studentProb(lower, upper, step, nu, M, estimate, d, mu, identity, rho, orthant, 1) for _ in range(2)]
    identElipsoid = [studentProb(lower, upper, step, nu, M, estimate, d, mu, identity, rho, elipsoid, 2) for _ in range(2)]
    oneFacOrthant = [studentProb(lower, upper, step, nu, M, estimate, d, mu, oneFactor, rho, orthant, 1) for _ in range(2)]
    oneFacElipsoid = [studentProb(lower, upper, step, nu, M, estimate, d, mu, oneFactor, rho, elipsoid, 2) for _ in range(2)]
    timeSpent = time.clock() - start_time
    pvantinew.append(timeSpent/8)
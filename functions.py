import numpy as np, scipy, math, itertools
import pandas as pd
from scipy.stats import chi


" ESTIMATORS "


# multivariate crude estimate
# if nu = 0, then simple normal estimate
def Crude(M, d, n, mu, sigma, region, regionNumber, nu, omega):
    r = np.random.multivariate_normal(mu, sigma, M)
    d = 0
    if nu == 0:
        for x in r:
            if region(x, regionNumber):
                d += 1
    else:
        for x in r:
            if region((math.sqrt(nu)/omega)*x, regionNumber):
                d += 1
    return d/M


# multivariate antithetic variates estimate
# M - number of runs
# if nu = 0, then simple normal estimate
def antithetic(M, d, n, mu, sigma, region, regionNumber, nu, omega):
    mu = np.array(mu)
    d = len(mu) # dimensija pagal kuria kuriam vidurkius ir kovariacija

    zeros = np.zeros(d)
    identity = np.identity(d)

    z = np.random.multivariate_normal(zeros, identity, M) # generuojam atsitiktinius dydzius

    gamma = np.linalg.cholesky(sigma)

    xPositive = [mu + (np.dot(gamma, elem)).T for elem in z]
    xNegative = [mu - (np.dot(gamma, elem)).T for elem in z]

    dPositive = 0
    dNegative = 0

    if nu == 0:
        for x in xPositive:
            if region(x, regionNumber):
                dPositive += 1

        for x in xNegative:
            if region(x, regionNumber):
                dNegative += 1

    else:
        for x in xPositive:
            if region((math.sqrt(nu)/omega)*x, regionNumber):
                dPositive += 1

        for x in xNegative:
            if region((math.sqrt(nu)/omega)*x, regionNumber):
                dNegative += 1
    return (dPositive+dNegative)/(2*M)


# functions for pV and pVantithetic functions

# T orthogonal matrix
# d - dimension
# m - montecarlo itterations number
def orthoT(d):
    a = np.random.rand(d, d)# for run in range(0, m)]
    b = scipy.linalg.qr(a)[0]# for matrix in a] # gram schmidt
    return np.matrix(b)


# central symmetric subset V
# d - dimension
# n - |V|
def unitV(d):
    file = 'C:/Users/Adomas/Dropbox/Bakalaurinis/vektoriai/vector'+str(d)+'.csv'
    vectors = pd.read_csv(file, sep=" ", header=None)
    return vectors.as_matrix()


# random chi
# d - dimension
# n - |V|

def radius(d, n):
    rv = chi.rvs(d, 0, 1, n) #for x in range(0,n)] #for y in range(0,m)
    return rv


# pV estimate
def pV(M, d, n, mu, sigma, region, regionNumber, nu, omega):
    k = []
    mu = np.transpose(np.matrix(mu))
    for i in range(0, M):

        T = orthoT(d)
        v = unitV(d)
        r = radius(d, v.shape[0])

        z = []
        [z.append(r[j]*np.dot(T, v[j])) for j in range(n)]

        gamma = np.linalg.cholesky(sigma)
        x = [mu + np.dot(gamma, np.transpose(elem)) for elem in z]

        win = 0
        for l in range(0,n):
            if region((math.sqrt(nu)/omega)*(np.array(x[l]).reshape(-1,).tolist()), regionNumber):
                win += 1
        k.append(win)
    return sum(k)/(M*n)


# pV w/ antithetic variates
def pVantithetic(M, d, n, mu, sigma, region, regionNumber, nu, omega):
    k = []
    mu = np.transpose(np.matrix(mu))
    for i in range(0,M):
        T = orthoT(d)
        v = unitV(d)
        r = radius(d, v.shape[0])

        zPositive = []
        zNegative = []
        for j in range(0,n):
            c = r[j]*np.dot(T, v[j])
            zPositive.append(c)
            zNegative.append(-c)

        gamma = np.linalg.cholesky(sigma)
        xPositive = [mu + np.dot(gamma, np.transpose(elem)) for elem in zPositive]
        xNegative = [mu + np.dot(gamma, np.transpose(elem)) for elem in zNegative]

        winPositive = 0
        winNegative = 0
        for l in range(0,n):
            if region((math.sqrt(nu)/omega)*(np.array(xPositive[l]).reshape(-1,).tolist()), regionNumber):
                winPositive += 1
            if region((math.sqrt(nu)/omega)*(np.array(xNegative[l]).reshape(-1,).tolist()), regionNumber):
                winNegative += 1
        k.append(winPositive)
        k.append(winNegative)
    return sum(k)/(2*M*n)


" COV MATRICES "

# in each, insert n & rho, receive sigma
# n - dimension, rho - value

# one factor
def oneFactor(n, rho):
    matrix = np.empty((n,n))
    for i in range(0,n):
        for j in range(0,n):
            if i == j:
                matrix[i, j] = 1
            else:
                matrix[i, j] = rho
    return (matrix)


# AR
def covAR(n, rho):
    matrix = np.empty((n,n))
    for i in range(0,n):
        for j in range(0,n):
            matrix[i, j] = rho ** math.fabs(i - j)
    return (matrix)


"Regions"


# in each insert x and set number of area
# Elipsoid
def elipsoid(x, regionNumber):
    if regionNumber == 1:
        b = np.array([1])
        b = np.append(b, np.repeat(0, len(x)-1))
    elif regionNumber == 2:
        b = np.array([0.5])
        b = np.append(b, np.repeat(0, len(x)-1))
    else:
        b = np.repeat(1, len(x))

    y = x - b
    np.dot(y, y) <= 1

    return np.dot(y,y)<=1


# Orthant
def orthant(x, regionNumber):
    if regionNumber == 1:
        return all(np.array(x) <= 0)
    elif regionNumber == 2:
        return all(np.array(x) <= 1)
    else:
        return all(np.array(x) <= -1)


# Rectangular
def rectangular(x, regionNumber):
    if regionNumber == 1:
        return all(-1 < np.array(x)) & all(np.array(x) < 1)
    elif regionNumber == 2:
        return all(0 < np.array(x)) & all(np.array(x) < 2)
    else:
        return all(0.5 < np.array(x)) & all(np.array(x) < 1.5)


" GOING FOR A STUDENT "


# the last function to integrate for student
def approxFunction(nu, omega):
    return (omega ** (nu - 1))*(math.exp(-((omega ** 2)/2)))


# calculates students prob with selected estimate and region
# upperOmegaBound - upper bound until which integration is approximated
# nOmegas - number of integration approximation points
# nu - degrees of freedom
# M - number of inside runs
# estimate - function of estimate
# d - dimension of orthogonal matrix and v vectors length
# n - |V| number of unit vectors
# mu - vector of means
# sigma - cov matrix
# region - function of region
# regionNumber - region number
def studentProb(upperOmegaBound, nOmegas, nu, M, estimate, d, n, mu, sigma, region, regionNumber):
    omegaX = np.linspace(0.00001, upperOmegaBound, nOmegas)  # points on X axis for integration approximation
    step = upperOmegaBound/nOmegas  # increase of each step

    normalProbabilities = []
    [normalProbabilities.append(estimate(M, d, n, mu, sigma, region, regionNumber, nu, omegaX[i])) for i in range(0, len(omegaX))]

    approxBlocks = []
    [approxBlocks.append(step*normalProbabilities[i]*approxFunction(nu, omegaX[i])) for i in range(0, len(omegaX))]
    approx = sum(approxBlocks)

    multiplier = (2 ** (1 - (nu/2)))/(math.gamma(nu/2))
    return multiplier*approx

# reads and returns true unit vectors
def unitV(d):
    file = 'C:/Users/Adomas/Dropbox/Bakalaurinis/vektoriai/vector'+str(d)+'.csv'
    vectors = pd.read_csv(file, sep=" ", header=None)
    return vectors.as_matrix()
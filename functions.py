import numpy as np, scipy, math, itertools
import pandas as pd
from numpy import matlib
from scipy.stats import chi
from scipy import integrate
from pip.util import Inf
from functions import *
import numpy as np
import itertools
import math
import scipy
from scipy.stats import chi
import time
from scipy.integrate import quad
from scipy import integrate
import matplotlib



" ESTIMATORS "


# multivariate crude estimate
def Crude(M, d, mu, sigma, rho, region, regionNumber, nu, omega):
    r = np.random.multivariate_normal(mu, sigma(d, rho), M)
    d = 0
    for x in r:
        if region((math.sqrt(nu) / omega) * x, regionNumber):
            d += 1
    return d / M


# multivariate antithetic variates estimate
# M - number of runs
def antithetic(M, d, mu, sigma, rho, region, regionNumber, nu, omega):
    zeros = np.zeros(d)
    identityMatrix = np.identity(d)
    mu = np.array(mu)
    gamma = np.linalg.cholesky(sigma(d, rho))

    z = np.random.multivariate_normal(zeros, identityMatrix, M)  # generuojam atsitiktinius dydzius

    xPositive = [mu + np.squeeze(np.array(np.dot(gamma, elem))) for elem in z]
    xNegative = [mu - np.squeeze(np.array(np.dot(gamma, elem))) for elem in z]

    dPositive = 0
    dNegative = 0

    for x in xPositive:
        if region((math.sqrt(nu) / omega) * x, regionNumber):
            dPositive += 1

    for x in xNegative:
        if region((math.sqrt(nu) / omega) * x, regionNumber):
            dNegative += 1

    return (dPositive + dNegative) / (2 * M)


# functions for pV and pVantithetic functions

# T orthogonal matrix
# d - dimension
# m - montecarlo itterations number
def orthoT(d):
    a = np.random.rand(d, d)  # for run in range(0, m)]
    b = scipy.linalg.qr(a)[0]  # for matrix in a] # gram schmidt
    return np.matrix(b)


# central symmetric subset V
# d - dimension
# n - |V|
def unitV(d):
    file = 'C:/Users/Adomas/Dropbox/Bakalaurinis/vektoriai/vector' + str(d) + '.csv'
    vectors = pd.read_csv(file, sep=" ", header=None)
    vectors = vectors.as_matrix()
    return vectors


# random chi
# d - dimension
# n - |V|
def radius(d, n):
    rv = chi.rvs(d, 0, 1, n)  #for x in range(0,n)] #for y in range(0,m)
    return rv


# pV estimate
def pV(M, d, mu, sigma, rho, region, regionNumber, nu, omega):

    k = []
    v = unitV(d)

    gamma = np.linalg.cholesky(sigma(d, rho))

    for i in range(0, M):
        T = orthoT(d)
        r = radius(d, v.shape[0])

        z = []
        [z.append(np.squeeze(np.array(r[j] * np.dot(T, v[j])))) for j in range(v.shape[0])]
        x = [mu + np.squeeze(np.array((np.dot(gamma, elem)))) for elem in z]
        win = 0
        for l in range(0, v.shape[0]):
            if region((math.sqrt(nu) / omega) * x[l], regionNumber):
                win += 1
        k.append(win)
    return sum(k) / (M * v.shape[0])

# pV w/ antithetic variates
def pVantithetic(M, d, mu, sigma, rho, region, regionNumber, nu, omega):
    k = []
    for i in range(0, M):
        T = orthoT(d)
        v = unitV(d)
        r = radius(d, v.shape[0])

        zPositive = []
        zNegative = []
        for j in range(0, v.shape[0]):
            c = np.squeeze(np.array(r[j] * np.dot(T, v[j])))
            zPositive.append(c)
            zNegative.append(-c)

        gamma = np.linalg.cholesky(sigma(d, rho))
        xPositive = [mu + np.squeeze(np.array((np.dot(gamma, elem)))) for elem in zPositive]
        xNegative = [mu + np.squeeze(np.array((np.dot(gamma, elem)))) for elem in zNegative]

        winPositive = 0
        winNegative = 0
        for l in range(0, v.shape[0]):
            if region((math.sqrt(nu) / omega) * xPositive[l], regionNumber):
                winPositive += 1
            if region((math.sqrt(nu) / omega) * xNegative[l], regionNumber):
                winNegative += 1
        k.append(winPositive)
        k.append(winNegative)
    return sum(k) / (2 * M * v.shape[0])

def pVantitheticNew(M, d, mu, sigma, rho, region, regionNumber, nu, omega):

    k = []

    vectors = unitV(d)
    v = []
    gamma = np.linalg.cholesky(sigma(d, rho))

    for vector in vectors:
        for x in vector:
            if x > 0:
                v.append(vector)
                break
            elif x < 0:
                break

    for i in range(0, M):
        T = orthoT(d)
        r = radius(d, len(v))
        zPositive = []
        zNegative = []

        for j in range(0, len(v)):
            c = np.squeeze(np.array(r[j] * np.dot(T, v[j])))
            zPositive.append(c)
            zNegative.append(-c)

        xPositive = [mu + np.squeeze(np.array((np.dot(gamma, elem)))) for elem in zPositive]
        xNegative = [mu + np.squeeze(np.array((np.dot(gamma, elem)))) for elem in zNegative]

        winPositive = 0
        winNegative = 0
        for l in range(0, len(v)):
            if region((math.sqrt(nu) / omega) * xPositive[l], regionNumber):
                winPositive += 1
            if region((math.sqrt(nu) / omega) * xNegative[l], regionNumber):
                winNegative += 1
        k.append(winPositive)
        k.append(winNegative)
    return sum(k) / (2 * M * len(v))

def pStar(M, d, mu, sigma, rho, region, regionNumber, nu, omega):
    gamma = sigma(d, rho)
    if region == elipsoid:
        win = []
        for i in range(M):
            T = orthoT(d)
            v = unitV(d)
            inRegion = [2*(math.sqrt(nu)/omega)*np.dot(T, vector).item(0) for vector in v if np.dot(T, vector).item(0) >= 0]
            win.append(sum([chi.cdf(value, d) for value in inRegion]))
    else:
        win = [0]
        for i in range(M):
            T = orthoT(d)
            v = unitV(d)
            Tv = [np.dot(T, vector) for vector in v]
            for vector in Tv:
                if (np.array(np.dot(vector, gamma) * (math.sqrt(nu) / omega)) <= 0).all():
                    win.append(1)
    return sum(win)/(M*len(v))

" COV MATRICES "

# in each, insert n & rho, receive sigma
# n - dimension, rho - value

# one factor
def oneFactor(n, rho):
    matrix = np.empty((n, n))
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                matrix[i, j] = 1
            else:
                matrix[i, j] = rho
    return (matrix)


# AR
def covAR(n, rho):
    matrix = np.empty((n, n))
    for i in range(0, n):
        for j in range(0, n):
            matrix[i, j] = rho ** math.fabs(i - j)
    return (matrix)


# identity
def identity(n, rho):
    return np.matlib.identity(n)


"Regions"


# in each insert x and set number of area
# Elipsoid
def elipsoid(x, regionNumber):
    if regionNumber == 1:
        b = np.array([1])
        b = np.append(b, np.repeat(0, len(x) - 1))
    elif regionNumber == 2:
        b = np.array([0.5])
        b = np.append(b, np.repeat(0, len(x) - 1))
    else:
        b = np.repeat(1, len(x))

    y = x - b
    np.dot(y, y) <= 1

    return np.dot(y, y) <= 1


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
    return (omega ** (nu - 1)) * (math.exp(-((omega ** 2) / 2)))

# function inside integral
def innerFunction(omega, nu):
    return (omega ** (nu - 1))*(math.exp(-((omega ** 2)/2)))

# give nu and criteria how much you allow to be near zero and lowerbound will be given
def determineLowerBound(nu, criteria):
    testPoints = np.arange(0.0, 5.0, 0.1)
    testResults = []
    [testResults.append(innerFunction(testPoints[i], nu)) for i in range(len(testPoints))]
    return testPoints[np.max(np.where(np.array(testResults) < criteria))]

# give nu and lower from determinelowerbound and criteria, upperbound will be given
def determineUpperBound(nu, lower, criteria):
    testPoints = np.arange(lower, 20.0, 0.1)
    testResults = []
    [testResults.append(quad(innerFunction, testPoints[i], np.inf, args=nu)[0]) for i in range(len(testPoints))]
    return testPoints[np.min(np.where(np.array(testResults) < criteria))]

# give evything, optimal step will be given
def determineStep(nu, lower, upper, initStep, criteria):
    last = 0
    while True:
        testPoints = np.arange(lower, upper, initStep)
        testResults = []
        [testResults.append(innerFunction(testPoints[i], nu)) for i in range(len(testPoints))]
        if math.fabs(integrate.simps(testResults, testPoints) - last) < criteria:
            break
        else:
            last = integrate.simps(testResults, testPoints)
            initStep -= 0.05
    return initStep


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
def studentProbOld(upperOmegaBound, nOmegas, nu, M, estimate, d, mu, sigma, rho, region, regionNumber):
    omegaX = np.linspace(0.00001, upperOmegaBound, nOmegas)  # points on X axis for integration approximation
    step = upperOmegaBound / nOmegas  # increase of each step

    normalProbabilities = []
    [normalProbabilities.append(estimate(M, d, mu, sigma, rho, region, regionNumber, nu, omegaX[i])) for i in
     range(0, len(omegaX))]

    approxBlocks = []
    [approxBlocks.append(step * normalProbabilities[i] * approxFunction(nu, omegaX[i])) for i in range(0, len(omegaX))]
    approx = sum(approxBlocks)

    multiplier = (2 ** (1 - (nu / 2))) / (math.gamma(nu / 2))
    return multiplier * approx


# new version
def studentProb(lower, upper, step, nu, M, estimate, d, mu, sigma, rho, region, regionNumber):
    omega = np.arange(lower, upper, step)  # points on X axis for integration approximation

    normalProbabilities = []
    [normalProbabilities.append(estimate(M, d, mu, sigma, rho, region, regionNumber, nu, omega[i])) for i in range(0, len(omega))]

    y = []
    [y.append(normalProbabilities[i]*innerFunction(omega[i], nu)) for i in range(len(omega))]

    approx = integrate.simps(y, omega)

    multiplier = (2 ** (1 - (nu / 2))) / (math.gamma(nu / 2))

    return multiplier * approx


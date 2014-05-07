import numpy as np
import scipy, math
from scipy.stats import chi


# multivariate crude estimate

def multiNormalCrude(n, mu, sigma, region, set):
    r = np.random.multivariate_normal(mu, sigma, n)
    d = 0
    for x in r:
        if region(x, set):
            d += 1
    return d/n


# multivariate AT estimator
def multiNormalAT(n, mu, sigma, region, set):
    mu = np.array(mu)
    d = len(mu) # dimensija pagal kuria kuriam vidurkius ir kovariacija

    zeros = np.zeros(d)
    identity = np.identity(d)

    z = np.random.multivariate_normal(zeros,identity,n) # generuojam atsitiktinius dydzius

    gamma = np.linalg.cholesky(sigma)

    xPositive = [mu + (np.dot(gamma,elem)).T for elem in z]
    xNegative = [mu - (np.dot(gamma,elem)).T for elem in z]

    dPositive = 0
    dNegative = 0
    for x in xPositive:
        if region(x, set):
            dPositive += 1

    for x in xNegative:
        if region(x, set):
            dNegative += 1

    return (dPositive+dNegative)/(2*n)


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
def unitVectors(d, n):
    X = [np.random.normal(0, 1, d) for x in range(0, n)]
    R = [(math.sqrt(sum([elem**2 for elem in xCord]))) for xCord in X]
    for i in range(0,n):
        X[i] = X[i]/R[i]
    return np.array(X)

# random chi
# d - dimension
# n - |V|
# m - montecarlo itterations number
def radius(d, n):
    rv = chi.rvs(d, 0, 1, n) #for x in range(0,n)] #for y in range(0,m)
    return rv


# z values
def pV(M, d, n, mu, sigma, region, set):
    k = []
    mu = np.transpose(np.matrix(mu))
    for i in range(0,M):
        r = radius(d, n)
        T = orthoT(d)
        v = unitVectors(d, n)

        z = []
        for j in range(0,n):
            c = r[j]*np.dot(T, v[j])
            z.append(c)

        gamma = np.linalg.cholesky(sigma)
        x = [mu + np.dot(gamma, np.transpose(elem)) for elem in z]

        win = 0
        for l in range(0,n):
            if region(np.array(np.array(x[l]).reshape(-1,).tolist()), set):
                win += 1
        k.append(win)
    return sum(k)/(M*n)


# pV with athitetic variates
def pVAT(M, d, n, mu, sigma, region, set):
    k = []
    mu = np.transpose(np.matrix(mu))
    for i in range(0,M):
        r = radius(d, n)
        T = orthoT(d)
        v = unitVectors(d, n)

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
            if region(np.array(xPositive[l]).reshape(-1,).tolist(), set):
                winPositive += 1
            if region(np.array(xNegative[l]).reshape(-1,).tolist(), set):
                winNegative += 1
        k.append(winPositive)
        k.append(winNegative)
    return sum(k)/(2*M*n)

"Covariance matrices"

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


# Elipsoid
def elipsoid(x, set):
    if set == 1:
        b = np.array([1])
        b = np.append(b, np.repeat(0, len(x)-1))
    elif set == 2:
        b = np.array([0.5])
        b = np.append(b, np.repeat(0, len(x)-1))
    else:
        b = np.repeat(1, len(x))

    y = x - b
    np.dot(y, y) <= 1

    return np.dot(y,y)<=1


# Orthant
def orthant(x, set):
    if set == 1:
        return all(x <= 0)
    elif set == 2:
        return all(x <= 1)
    else:
        return all(x <= -1)


# Rectangular
def rectangular(x, set):
    if set == 1:
        return all(-1 < np.array(x)) & all(np.array(x) < 1)
    elif set == 2:
        return all(0 < np.array(x)) & all(np.array(x) < 2)
    else:
        return all(0.5 < np.array(x)) & all(np.array(x) < 1.5)
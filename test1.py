from functions import *

def CrudeNorm(M, d, mu, sigma, rho, region, regionNumber, nu, omega):
    r = np.random.multivariate_normal(mu, sigma(d, rho), M)
    d = 0
    for x in r:
        if region( x, regionNumber):
            d += 1
    return d / M

def pStarN(M, d, mu, sigma, rho, region, regionNumber, nu, omega):
    gamma = sigma(d, rho)
    if region == elipsoid:
        win = []
        for i in range(M):
            T = orthoT(d)
            v = unitV(d)
            inRegion = [2*np.dot(T, vector).item(0) for vector in v if np.dot(T, vector).item(0) >= 0]
            win.append(sum([chi.cdf(value, d) for value in inRegion]))
    return sum(win)/(M*len(v))

Crude = [CrudeNorm(500, 2, [0,0], identity, 0.1, elipsoid, 2, 0.5, 2) for i in range(5000)]
pStar1 = [pStarN(500, 2, [0,0], identity, 0.1, elipsoid, 2, 0.5, 2) for i in range(250)]

0.00044326335984000399

cVar = np.var(Crude[:250])
pVar = np.var(pStar1)
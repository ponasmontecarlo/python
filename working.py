from normalUniFunc import oneFactor, covAR, elipsoid,orthant,rectangular, pV, multiNormalAT, radius, orthoT, unitVectors, multiNormalCrude, multiNormalAT
import numpy as np

#b = np.array([1, 0])
x = np.array([0.2, 0.3])

#print(rectangular(x, 3))

d = 3
n = 5
rho = 0.1
t = [0.5, 0.5, 0.5]
mu = [0, 0, 0]
sigma = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]



a = multiNormalCrude(10000, mu, sigma, elipsoid, 1)
b = multiNormalAT(5000, mu, sigma, elipsoid, 1)
print((a- a**2)/(b - b ** 2))
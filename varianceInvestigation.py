import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from os import listdir
from os.path import isfile, join
from functions import *


###################
nu = 2
lower = 0.015
upper = 4.315
step = 0.2
sigma = identity
rho = 0.1
region = orthant
regionNumber = 1
###################

C2 = [[] for _ in range(10)]
for i in range(10):
    C2[i] = np.array([studentProb(lower, upper, step, nu, M, Crude, 2, [0, 0], sigma, rho, region, regionNumber) for M in range(1, 5)])

C2df = pd.DataFrame(np.matrix(C2).T)
C2df.to_csv('C:/Users/Adomas/Dropbox/Bakalaurinis/varInvest2.txt', header=False, index=False)

C3 = [[] for _ in range(10)]
for i in range(10):
    C3[i] = np.array([studentProb(lower, upper, step, nu, M, Crude, 3, [0, 0, 0], sigma, rho, region, regionNumber) for M in range(1, 1001)])

C3df = pd.DataFrame(np.matrix(C3).T)
C3df.to_csv('C:/Users/Adomas/Dropbox/Bakalaurinis/varInvest3.txt', header=False, index=False)

C5 = [[] for _ in range(10)]
for i in range(10):
    C5[i] = np.array([studentProb(lower, upper, step, nu, M, Crude, 5, [0, 0, 0, 0, 0], sigma, rho, region, regionNumber) for M in range(1, 1001)])
C5df = pd.DataFrame(np.matrix(C5).T)
C5df.to_csv('C:/Users/Adomas/Dropbox/Bakalaurinis/varInvest5.txt', header=False, index=False)

#### TEMP

# C = np.matrix([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10])
# Cdim2 = pd.DataFrame(C.T)
# Cdim2.to_csv('C:/Users/Adomas/Dropbox/Bakalaurinis/varInvest.txt', header=False, index=False)

####

marginC2 = [[] for _ in range(10)]
marginC3 = [[] for _ in range(10)]
marginC5 = [[] for _ in range(10)]


for j in range(10):
    for i in range(999):
        marginC2[j].append((C2df.iloc[i+1, j]-C2df.iloc[i, j])/C2df.iloc[i, j])
        marginC3[j].append((C3df.iloc[i+1, j]-C3df.iloc[i, j])/C3df.iloc[i, j])
        marginC5[j].append((C5df.iloc[i+1, j]-C5df.iloc[i, j])/C5df.iloc[i, j])
#
# [plt.plot(np.abs(marginC[i][5:]), 'ro') for i in range(10)]
# plt.plot(np.repeat(0.1, 994))
# plt.show()
#
#
# cDiff = np.diff(c1)
# plt.plot(c1)
# plt.plot(cDiff)
# plt.show()
#
# cDiffabs = np.abs(cDiff)
# plt.plot(cDiffabs)
# plt.show()
#
# plt.plot(np.repeat(0.01, 1000))
# plt.show()

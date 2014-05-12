from functions import *
import numpy as np
import itertools
import math
import scipy
from scipy.stats import chi
import scipy.integrate
import time

#### PARAMETERS ####
upperOmegaBound = 10
nOmegas = 200
nu = 5
M = 250
d = 3
rho = 0.1
#mu = [0, 0, 0, 0]
mu = [0, 0, 0]
#sigma = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
sigma = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
estimate = pV
region = orthant
regionNumber = 1
#####################

# tic = time.clock()
# print(studentProb(upperOmegaBound, nOmegas, nu, M, estimate, d, mu, sigma, region, regionNumber))
# toc = time.clock()
# print('Elapsed time = ', (toc - tic), 'seconds')
#
# with open('home/adomas/Dropbox/Bakalaurinis/results/test.txt', 'a') as file:
#     file.write('input')


lines = [1,2,3,4,5,6,7]


myfile = open('/home/adomas/Dropbox/Bakalaurinis/results/test.txt', 'w')
for line in lines:
    var1 = line*2
    myfile.write("%s\n" % var1)

myfile.close()
#text_file.close()



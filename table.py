from os import listdir
from os.path import isfile, join
from collections import Counter
import re
import pandas as pd
import numpy as np

#true dir
#directory = 'C:/Users/Adomas/Dropbox/Bakalaurinis/results/'
# test dir
directory = 'C:/Users/Adomas/Dropbox/Bakalaurinis/resultsBad/'


filesAll = [file for file in listdir(directory) if isfile(join(directory, file))]
# filesAllParsed = [file.partition('_')[2] for file in filesAll]
#
# freq = Counter(filesAllParsed)  # creates dict of files and frequencies
#
# files = [file for file, frequency in freq.items() if frequency == 4]  # selects only which appear 4 times



# select nu and dim
nu = 0.5
dim = 3

regex = 'dim%s_df%s' % (dim, nu)
pattern = re.compile(regex, re.I)
matched = [file for file in filesAll if re.search(pattern, file)]
print('Per mazai failu') if len(matched)<16 else print('Pakanka failu')
[print('Blagai') for file in matched if pd.read_table(directory+file).shape[0] == 500]

# kombinacijos
combCrude = [['Crude', 'orthant1'], ['Crude', 'elipsoid2']]
combAntithetic = [['Antithetic', 'orthant1'], ['Antithetic', 'elipsoid2']]
combPV = [['PV', 'orthant1'], ['PV', 'elipsoid2']]
combPVantithetic = [['pVantithetic', 'orthant1'], ['pVantitheticNew', 'elipsoid2']]


Crude = np.array([np.average([np.var(pd.read_table(directory+file, header=None).ix[:, 0]) for file in matched if all(comb in file for comb in combCrude[i])]) for i in range(2)])
Antithetic = np.array([np.average([np.var(pd.read_table(directory+file, header=None).ix[:, 0]) for file in matched if all(comb in file for comb in combAntithetic[i])]) for i in range(2)])
PV = np.array([np.average([np.var(pd.read_table(directory+file, header=None).ix[:, 0]) for file in matched if all(comb in file for comb in combPV[i])]) for i in range(2)])
PVantithetic = np.array([np.average([np.var(pd.read_table(directory+file, header=None).ix[:, 0]) for file in matched if all(comb in file for comb in combPVantithetic[i])]) for i in range(2)])

final_matrix = np.matrix([Crude/Antithetic, Crude/PV, Crude/PVantithetic])

final_df = pd.DataFrame(final_matrix.T, columns=['Antithetic', 'pV', 'pVantithetic'], index=['O', 'E'])
final_df.to_csv(directory+'table.txt')
final_df

from os import listdir
from os.path import isfile, join
from collections import Counter
import re
import pandas as pd
import numpy as np

#### PARAMETERS #####
dim = 5
nu = 7
directory = 'C:/Users/Adomas/Dropbox/Bakalaurinis/tables/%s/dim%s/' % (nu, dim)
#####################

# creating data
filesAll = [file for file in listdir(directory) if isfile(join(directory, file))]

Full = []
tooFull = []
notFull = []
for file in filesAll:
    if (pd.read_table(directory+file, header=None)).shape[0] == 500:
        Full.append(file)
    elif (pd.read_table(directory+file, header=None)).shape[0] > 500:
        tooFull.append(file)
    else:
        notFull.append(file)

##### too full #####
for file in tooFull:
    data = pd.read_table(directory+file, header=None)
    newData = pd.DataFrame(np.random.choice(data.ix[:, 0], 500))
    newData.to_csv(directory+file, header=False, index=False)

##### not full #####
for file in notFull:
    data = pd.read_table(directory+file, header=None)
    newData = pd.DataFrame(np.random.choice(data.ix[:, 0], 500, replace=True))
    newData.to_csv(directory+file, header=False, index=False)

# making table

regex = 'dim%s_df%s' % (dim, nu)
pattern = re.compile(regex, re.I)
matched = [file for file in filesAll if re.search(pattern, file)]
#print('Per mazai failu') if len(matched)<16 else print('Pakanka failu')
#[print('Blagai') for file in matched if pd.read_table(directory+file).shape[0] == 500]

# kombinacijos
combCrude = [['Crude', 'orthant1'], ['Crude', 'elipsoid2']]
combAntithetic = [['Antithetic', 'orthant1'], ['Antithetic', 'elipsoid2']]
combPV = [['PV', 'orthant1'], ['PV', 'elipsoid2']]
combPVantithetic = [['pVantitheticNew', 'orthant1'], ['pVantitheticNew', 'elipsoid2']]
combPstar = [['pStar', 'orthant1'], ['pStar', 'elipsoid2']]

Crude = np.array([np.average([np.var(pd.read_table(directory+file, header=None).ix[:, 0]) for file in matched if all(comb in file for comb in combCrude[i])]) for i in range(2)])
Antithetic = np.array([np.average([np.var(pd.read_table(directory+file, header=None).ix[:, 0]) for file in matched if all(comb in file for comb in combAntithetic[i])]) for i in range(2)])
PV = np.array([np.average([np.var(pd.read_table(directory+file, header=None).ix[:, 0]) for file in matched if all(comb in file for comb in combPV[i])]) for i in range(2)])
PVantithetic = np.array([np.average([np.var(pd.read_table(directory+file, header=None).ix[:, 0]) for file in matched if all(comb in file for comb in combPVantithetic[i])]) for i in range(2)])
Pstar = np.array([np.average([np.var(pd.read_table(directory+file, header=None).ix[:, 0]) for file in matched if all(comb in file for comb in combPstar[i])]) for i in range(2)])

#final_matrix = np.matrix([Crude/Antithetic, Crude/PV])#,Crude/PVantithetic])
final_matrix = np.matrix([Crude/Antithetic, Crude/PV,Crude/PVantithetic, Crude/Pstar])

#final_df = pd.DataFrame(final_matrix.T, columns=['Antithetic', 'pV'], index=['O', 'E'])
final_df = pd.DataFrame(final_matrix.T, columns=['Antithetic', 'pV', 'pVantithetic', 'pStar'], index=['O', 'E'])

final_df.to_csv('C:/Users/Adomas/Dropbox/Bakalaurinis/tables/output/table_nu%s_dim%s.txt' % (nu, dim))
print(final_df)


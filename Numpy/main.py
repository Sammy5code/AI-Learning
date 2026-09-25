import numpy as np

data = np.array([[1, 2], [3, 4]], dtype=int)
np.savetxt('csvdata.csv', data)
print(np.loadtxt('csvdata.csv'))

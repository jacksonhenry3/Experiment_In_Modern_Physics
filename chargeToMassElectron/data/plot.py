import numpy as np
import matplotlib.pyplot as plt 

data1 = np.loadtxt('197.5V.txt',skiprows = 1)
data2 = np.loadtxt('256.9V.txt',skiprows = 1)
data3= np.loadtxt('299.8V.txt',skiprows = 1)
data4 = np.loadtxt('345V.txt',skiprows = 1)

print data1.shape
print data2.shape
np.append(data1,data2,1)
np.append(data1,data3,1)
np.append(data1,data4,1)

np.savetxt('data.txt',data1)
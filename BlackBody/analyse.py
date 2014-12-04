import numpy as np
import matplotlib.pyplot as plt

def normalize(l):
	return(l/np.max(l))

data = np.transpose(np.loadtxt('BlackBody600.data',skiprows = 3))

plt.plot(data[0]*1.20,normalize(data[1]),'r.')
plt.error(data[0]*1.20,normalize(data[3]),'g.')

data = np.transpose(np.loadtxt('BlackBody800.data',skiprows = 3))

plt.plot(data[0]*1.20,normalize(data[1]),'b.')
plt.plot(data[0]*1.20,normalize(data[3]),'g.')

data = np.transpose(np.loadtxt('BlackBody1600.data',skiprows = 3))

plt.plot(data[0]*1.20,normalize(data[1]),'k.')
plt.plot(data[0]*1.20,normalize(data[3]),'g.')

data = np.transpose(np.loadtxt('BlackBody1600.data',skiprows = 3))

plt.plot(data[0]*1.20,normalize(data[1]),'y.')
plt.plot(data[0]*1.20,normalize(data[3]),'g.')

plt.show()
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op
data = np.transpose(np.loadtxt('dataForGnu.txt',skiprows = 1))
x = np.linspace(.001,1000,10000)
for i in range(-3,3):
	s = 2*10**(-13)
	plt.plot(x,s*x**(1+i/10.))
plt.plot(data[0],data[1])
plt.show()
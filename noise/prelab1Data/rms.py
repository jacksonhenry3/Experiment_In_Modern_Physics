import numpy as np 
import matplotlib.pyplot as plt 
data = np.transpose(np.loadtxt("data.csv",delimiter = ','))
RMS =  np.sqrt(np.sum(data[1]**2)/2482)
print RMS
plt.plot(data[0],data[1],'b.')
plt.show()
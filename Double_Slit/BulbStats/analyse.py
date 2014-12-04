import numpy as np 
import matplotlib.pyplot as plt 
data = np.transpose(np.loadtxt('10SecondDeviation.txt',skiprows = 1))

plt.plot(data[0],data[3],'.')
plt.xlabel('Counts')
plt.ylabel('Percent Error')
plt.title('10 Second Percent Error')


# plotData(DS,'','r')

plt.show()
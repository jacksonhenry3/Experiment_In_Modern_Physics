import numpy as np 
import matplotlib.pyplot as plt 
DS = np.transpose(np.loadtxt('DoubleSlit.txt',skiprows = 1))


plt.plot(position,intensity,color+'-')
plt.plot(position,intensity,color+'.')
plt.xlabel('angle (degrees)')
plt.ylabel('Normalized Intensity')
plt.title(title)


plotData(DS,'','r')
plotData(SS,'Bulb Data','b')
plt.show()
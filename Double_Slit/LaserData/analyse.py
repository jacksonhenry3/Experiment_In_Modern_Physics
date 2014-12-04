import numpy as np 
import matplotlib.pyplot as plt 
DS = np.transpose(np.loadtxt('DoubleSlit.txt',skiprows = 1))
SS1 = np.transpose(np.loadtxt('SingleSlit1.txt',skiprows = 1))
SS2 = np.transpose(np.loadtxt('SingleSlit2.txt',skiprows = 1))

def plotData(data,title,color):
	position = np.degrees((data[0]-np.median(data[0]))/500)
	intensity = data[1]/(np.max(data[1]))
	plt.plot(position,intensity,color+'-')
	plt.plot(position,intensity,color+'.')
	plt.xlabel('angle (degrees)')
	plt.ylabel('Normalized Intensity')
	plt.title(title)
	

plotData(DS,'','r')
plotData(SS1,'','g')
plotData(SS2,'Laser Data','b')
plt.show()
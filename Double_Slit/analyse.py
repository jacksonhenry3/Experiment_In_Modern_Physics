import numpy as np 
import matplotlib.pyplot as plt 
DSLaser = np.transpose(np.loadtxt('DSLaser.txt',skiprows = 1))
# SingleSlitLowIntensity = np.transpose(np.loadtxt('SingleSlitLowIntensity.txt',skiprows = 1))
# LowInteensityBulbDoubleSlit = np.transpose(np.loadtxt('LowInteensityBulbDoubleSlit.txt',skiprows = 1))

def plotData(data,title):
	position  = np.arctan((data[0]-np.median(data[0]))/50)
	intensity = data[1]/(np.max(data[1]))
	plt.plot(position,intensity)
	plt.xlabel('angle')
	plt.ylabel('Normalized Intensity')
	plt.title(title)
	plt.show()

plotData(DSLaser,'')
plotData(SingleSlitLowIntensity,'')
plotData(LowInteensityBulbDoubleSlit,'')

import numpy as np
import matplotlib.pyplot as plt

def getTemp(I,V):
	return(((V/I)/4.5398)**(1/1.203)*295)

def genCalcCols(dataFile):
	data = np.transpose(np.loadtxt(dataFile,skiprows = 1))
	T = getTemp(data[3],data[0]*1.2)
	titles = "Intensity	Volts (mv)	V err (mv)	current (A)	Temperature (K)	1/T (1/K)	log Vout	err %"
	arr1 = np.transpose(np.vstack([data[0:4],T,1./T,np.log(data[1]),data[2]/data[1],]))

	np.savetxt(dataFile,arr1,header = titles, fmt='%.7f',delimiter = '	')

def plotLogDetVinvT(dataFile,title):
	data = np.transpose(np.loadtxt(dataFile,skiprows = 1))
	T = getTemp(data[3],data[0]*1.2)
	plt.plot(data[5],data[6],'ko')
	plt.xlabel('1/T [1/k]')
	plt.ylabel('ln(data) [ln(v)]')
	plt.title(title)
	plt.savefig(dataFile[:-4]+'png')
	plt.close()

genCalcCols('BlackBody600.data')
genCalcCols('BlackBody800.data')
genCalcCols('BlackBody1200.data')
genCalcCols('BlackBody1600.data')
genCalcCols('BlackBody2000.data')
genCalcCols('BlackBody2400.data')
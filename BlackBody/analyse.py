import numpy as np
import matplotlib.pyplot as plt

sigma = 5.67*(10**(-8))

def normalize(l):
	return(l/np.max(l))


#NEEDS TO BE DISCUSSSEDSDESSDDS
def getTemp(I,V):
	alpha = 4.5*10**-3
	return(1/alpha*(V/I)/4.5398-1+295) #calues are reasonable, but got alpha from internets.
	return(((I*V)/sigma)**(1/4.)) #WHY DOESNT THIS WORK!!!!

def genCalcCols(dataFile):
	data = np.transpose(np.loadtxt(dataFile,skiprows = 1))
	T = getTemp(data[3],data[0]*1.2)
	titles = "Intensity	Volts (mv)	V err (mv)	current (A)	Temperature (K)	1/T (1/K)	log Vout"
	QUACK = np.transpose(np.vstack([data[0:4],T,1./T,np.log(data[1])]))
	np.savetxt(dataFile,QUACK,header = titles, fmt='%.7f',delimiter = '	')

def plotLogDetVinvT(dataFile,title):
	data = np.transpose(np.loadtxt(dataFile,skiprows = 1))
	T = getTemp(data[3],data[0]*1.2)
	plt.plot(data[5],data[6],'ko')
	plt.xlabel('1/T [1/k]')
	plt.ylabel('ln(data) [ln(v)]')
	plt.title(title)
	plt.savefig(dataFile[:-4]+'png')
	plt.close()



# genCalcCols('BlackBody600.data')
plotLogDetVinvT('BlackBody600.data','600 nm')

# genCalcCols('BlackBody800.data')
plotLogDetVinvT('BlackBody800.data','800 nm')

# genCalcCols('BlackBody1200.data')
plotLogDetVinvT('BlackBody1200.data','1200 nm')

# genCalcCols('BlackBody1600.data')
plotLogDetVinvT('BlackBody1600.data','1600 nm')

# genCalcCols('BlackBody2000.data')
plotLogDetVinvT('BlackBody2000.data','2000 nm')

# genCalcCols('BlackBody2400.data')
plotLogDetVinvT('BlackBody2400.data','2400 nm')

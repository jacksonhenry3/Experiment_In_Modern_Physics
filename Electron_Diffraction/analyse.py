import numpy as np 
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '../')
import error as er #get the error library
from sympy import Symbol,pi,sqrt #import required symbolic math components



#----------- constants-------------
c    = 299792458000 #in mm/s
Me   = 511 #KeV/c^2
h    = 4.13*10**(-18) #KeV s

d11  = 1.23*10**(-7) #latice spacing in mm
d10  = 2.13*10**(-7)

L    = 130 #Distance to source in mm
r    = 66 #radius of curvature of aparatus in mm
LErr = 2

header = 'Voltage (kV)|voltage err (kV)|small inner(mm)|small middle (mm)|small err (mm)|large inner (mm)|large middle (mm)|large err (mm)'
# ----------- raw data and raw error ---------
data = np.loadtxt('data.txt',skiprows = 1)
voltage     = data[:,0]
voltageErr  = data[:,1]
smallInner  = data[:,2]
smallMiddle = data[:,3]
smallErr    = data[:,4]
largeInner  = data[:,5]
largeMiddle = data[:,6]
largeErr    = data[:,7]

# ------------ functins to calculate values and errors----------
def Bragg(D,d,L = L,r = r):
	a       = np.sqrt(r**2-D**2/4)
	x       = (L/(L-(r-a))) #based on geometric calculations that can bee seen in my lab notebook
	D       = D+2*x
	theta   = np.arctan(D/(2*L))/2
	waveLen = 2*d*np.sin(theta)
	return(waveLen*10**6) #converts to nm

def DeBroglie(v,m = Me):
	from math import sqrt
	p       = sqrt(2*m)*np.sqrt(v)# the two sqrts is becouse of an issue with numpy
	waveLen = h/p*c # correct for wierd units with a factor of c
	return(waveLen*10**6) #converts to nm

def DeBroglieErr(voltage,voltageErr,m = Me):
	v = Symbol("v",positive = True) # initialize symbols
	h = Symbol("h",positive = True)
	c = Symbol("c",positive = True)
	m = Symbol("m",positive = True)
	from sympy import sqrt # initialize symbols
	waveLen    = h/(sqrt(2*m*v)*c)

	# get the error function
	func =  er.getRelError([v],waveLen)

	# calculate error for each point
	error = func(voltage,voltageErr)

	return error

def BraggErr(Diam,DiamErr,d,L = L,r = r):
	v = Symbol("v",positive = True) # initialize symbols
	D = Symbol("D",positive = True)
	L = Symbol("L",positive = True)

	from sympy import sqrt,atan,sin,pprint # initialize symbols
	a       = sqrt(r**2-D**2/4)
	x       = (L/(L-(r-a))-1)*D/2 #based on geometric calculations that can bee seen in my lab notebook
	DCorect = D+2*x
	theta   = DCorect/(2*L)/2
	waveLen = 2*d*theta

	# get the error function
	func =  er.getRelError([D,L],waveLen)

	# calculate error for each point
	error = func(voltage,130,voltageErr,2)

	return error
	
# ------------ generating the plots --------------
def plotWaveLengths(v,verr,D,d,title):
	global data
	global header
	plt.errorbar(v,DeBroglie(v),xerr = .02,yerr = DeBroglieErr(voltage,verr)*DeBroglie(v),fmt = 'b.', label = 'DeBroglie')
	plt.errorbar(v, Bragg(D,d),xerr = .02,yerr = BraggErr(smallInner,smallErr,d)*Bragg(D,d),fmt = 'r.',label = 'Bragg')
	a    =  np.expand_dims(Bragg(D,d),axis = 1)
	data = np.append(data,a,1)
	a    =  np.expand_dims(BraggErr(D,smallErr,d),axis = 1)
	data = np.append(data,a,1)
	header+= '|Bragg'+str(d)+'|Bragg'+str(d)+'err'
	plt.ylabel("wave length (nm)")
	plt.xlabel("Accelerating potential (Kv)")
	plt.title("Electron wavelengths, DeBroglie VS Bragg \n "+title)
	plt.legend(bbox_to_anchor=(.7, .95), loc=2, borderaxespad=0.)
	plt.savefig(title+'.pdf')
	plt.close("all")

plotWaveLengths(voltage,voltageErr,smallInner,d10,'Small_Ring_Inner_Diameter')
plotWaveLengths(voltage,voltageErr,smallMiddle,d10,'Small_Ring_Middle_Diameter')
plotWaveLengths(voltage,voltageErr,smallInner,d11,'Larg_Ring_Inner_Diameter')
plotWaveLengths(voltage,voltageErr,smallMiddle,d11,'Large_Ring_Middle_Diameter')

# calculate the average percent difference between debroglie and bragg WL
avDif = np.abs(1-Bragg(smallInner,d10)/DeBroglie(voltage))
avDif += np.abs(1-Bragg(smallMiddle,d10)/DeBroglie(voltage)) 
avDif += np.abs(1-Bragg(largeInner,d11)/DeBroglie(voltage))
avDif += np.abs(1-Bragg(largeMiddle,d11)/DeBroglie(voltage))
avDif = avDif/4

print np.std(avDif) # print the standard deviation of those percent differences
print np.mean(avDif)

a      =  np.expand_dims(DeBroglie(voltage),axis = 1)
data   = np.append(data,a,1)
a      =  np.expand_dims(DeBroglieErr(voltage,voltageErr),axis = 1)
data   = np.append(data,a,1)
header += '|DBWL'
header +='|DBWLErr'

a      =  np.expand_dims(avDif,axis = 1)
data   = np.append(data,a,1)
header +='|av % diff'

np.savetxt('dataWithCalculatedCols.txt',  np.transpose(data),newline = '\n \n', delimiter  = '  ', fmt = '%.2e'    )
print header
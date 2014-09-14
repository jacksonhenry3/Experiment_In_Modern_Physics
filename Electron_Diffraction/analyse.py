import numpy as np 
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '../')
import error as er #get the error library
from sympy import Symbol,pi,sqrt #import required symbolic math components



#----------- constants-------------
c = 299792458000 #in mm/s
Me = 511 #KeV/c^2
h  = 4.13*10**(-18) #KeV s

d11 = 1.23*10**(-7) #latice spacing in mm
d10 = 2.13*10**(-7)

L = 130 #Distance to source in mm
r = 66 #radius of curvature of aparatus in mm
LErr = 2

# ----------- raw data and raw error ---------
data = np.loadtxt('data.txt',skiprows = 1)
voltage = data[:,0]
voltageErr= data[:,1]
smallInner = data[:,2]
smallMiddle = data[:,3]
smallErr = data[:,4]
largeInner = data[:,5]
largeMiddle = data[:,6]
largeErr = data[:,7]

# ------------ calculated values----------
def Bragg(D,d,L = L,r = r):
	a = np.sqrt(r**2-D**2/4)
	x = (L/(L-(r-a))) #based on geometric calculations that can bee seen in my lab notebook
	D = D+2*x
	theta = np.arctan(D/(2*L))/2
	waveLen = 2*d*np.sin(theta)
	return(waveLen*10**6) #converts to nm

def DeBroglie(v,m = Me):
	from math import sqrt
	p = sqrt(2*m)*np.sqrt(v)# the two sqrts is becouse of an issue with numpy
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

	from sympy import sqrt,atan,sin,pprint # initialize symbols
	a = sqrt(r**2-D**2/4)
	x = (L/(L-(r-a))) #based on geometric calculations that can bee seen in my lab notebook
	DCorrected = D+2*x
	theta = DCorrected/(2*L)/2
	waveLen = 2*d*theta
	
	# get the error function
	func =  er.getRelError([D],waveLen)

	# calculate error for each point
	error = func(voltage,voltageErr)

	return error


# ------------ generating the plots --------------

def plotWaveLengths(v,verr,D,d,title):
	plt.errorbar(v,DeBroglie(v),xerr = .02,yerr = DeBroglieErr(voltage,verr)*DeBroglie(v),fmt = 'b.', label = 'DeBroglie')
	plt.errorbar(v, Bragg(D,d),xerr = .02,yerr = BraggErr(smallInner,smallErr,d)*Bragg(D,d),fmt = 'r.',label = 'Bragg')
	plt.ylabel("wave length (nm)")
	plt.xlabel("Accelerating potential (Kv)")
	plt.title("Electron wavelengths, DeBroglie VS Bragg \n "+title)
	plt.legend(bbox_to_anchor=(.7, .95), loc=2, borderaxespad=0.)
	plt.savefig(title+'.pdf')
	plt.close("all")

#Dont forget to calculate error in wave lengths (this require propogation of error, and its 1:45, i can't seem to figure it out.
plotWaveLengths(voltage,voltageErr,smallInner,d10,'Small_Ring_Inner_Diameter')
plotWaveLengths(voltage,voltageErr,smallMiddle,d10,'Small_Ring_Middle_Diameter')
plotWaveLengths(voltage,voltageErr,smallInner,d11,'Larg_Ring_Inner_Diameter')
plotWaveLengths(voltage,voltageErr,smallMiddle,d11,'Large_Ring_Middle_Diameter')
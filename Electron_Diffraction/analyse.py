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

def DeBroglieErr(v,dv,m = Me):
	from sympy.abc import v # initialize symbols
	waveLen    = h/(sqrt(2*m)*np.sqrt(v)*c)

	# get the error function
	func =  er.getError([x,y],f,showFunc = True)

	# measured values of variables and there errors
	x    = np.array([.0404,.05])
	dx   = np.array([.00031,.0004])
	y = np.array([1,2])
	dy = np.array([.1,.01])

	# calculate error for each point
	error = func(x,y,dx,dy)

	print error


# ------------ generating the plots --------------

def plotWaveLengths(v,D,d,DeBrogErr,BraggErr,title):
	plt.errorbar(v,DeBroglie(v),xerr = .02,yerr = DeBrogErr,fmt = 'b.', label = 'DeBroglie')
	plt.errorbar(v, Bragg(D,d),xerr = .02,yerr = BraggErr,fmt = 'r.',label = 'Bragg')
	plt.ylabel("wave length (nm)")
	plt.xlabel("Accelerating potential (Kv)")
	plt.title("Electron wavelengths, DeBroglie VS Bragg \n "+title)
	plt.legend(bbox_to_anchor=(.7, .95), loc=2, borderaxespad=0.)
	plt.savefig(title+'.pdf')
	plt.close("all")


#Dont forget to calculate error in wave lengths (this require propogation of error, and its 1:45, i can't seem to figure it out.
plotWaveLengths(voltage,smallInner,d10,0,0,'Small_Ring_Inner_Diameter')
plotWaveLengths(voltage,smallMiddle,d10,0,0,'Small_Ring_Middle_Diameter')
plotWaveLengths(voltage,smallInner,d11,0,0,'Larg_Ring_Inner_Diameter')
plotWaveLengths(voltage,smallMiddle,d11,0,0,'Large_Ring_Middle_Diameter')
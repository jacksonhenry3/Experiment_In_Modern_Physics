import numpy as np
import matplotlib.pyplot as plt

def angle(dataFile):
	data   = np.transpose(np.loadtxt(dataFile,skiprows = 1,usecols = (1,2,3,4)))
	angle = np.abs((data[0]+data[1]/60-(data[2]+data[3]/60))/2.)
	return angle

def wavelength(angle,order):
	d = 1600 #CHANGE THIS TO REFLECT ACTUAL VALUE OF DIFFRACTION GRATING USED  in nm
	return(d*np.sin(np.radians(angle))/order)

# theta2 = angle('HelliumFirstOrder.Data')
# theta3 = angle('HelliumSecondOrder.Data')
# He_wl1 = wavelength(theta2,1)
# He_wl2 = wavelength(theta3,2)
# He_wl  = (He_wl1+He_wl2)/2.

theta1 = angle('Hydrogen.Data')
H_wl   = wavelength(theta1,1)

coefs =  np.polyfit(1./np.arange(4,1,-1)**2,1/H_wl,1)
print coefs[1]/4
print -coefs[0]
plt.plot(1./np.arange(4,1,-1)**2,1/H_wl,'o')
plt.show()
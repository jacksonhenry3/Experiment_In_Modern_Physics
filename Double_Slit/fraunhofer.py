from numpy import pi,sin,cos,arange
import matplotlib.pyplot as plt 

def normalised_intensity(angle,a,d,wave_length):
	lambdam = wave_length*10**(-9)
	c       = pi*sin(angle)/lambdam;
	alpha   = c*(a*.001);
	beta    = c*(d*.001);
	I       = ((cos(beta))**2.)*((sin(alpha))/alpha)**2.;
	return(I)

a = .085 # in mm
d = .350 # in mm
WL = 670 # in nm

angle = arange(-.01,.01,.00001)
normI = normalised_intensity(angle,a,d,WL)
plt.plot(angle,normI)

plt.title('Initial Given Values')
plt.ylabel('Normalised Intensity')
plt.xlabel('angle (radians)')
plt.savefig('all_stadard_values.png')
plt.close()


normI = normalised_intensity(angle,2*a,d,WL)
plt.plot(angle,normI)

normI = normalised_intensity(angle,a/2,d,WL)
plt.plot(angle,normI)

plt.title('Effects of Varying Slit Width')
plt.ylabel('Normalised Intensity')
plt.xlabel('angle (radians)')
plt.savefig('varying_a.png')
plt.close()

normI = normalised_intensity(angle,a,2*d,WL)
plt.plot(angle,normI)

normI = normalised_intensity(angle,a,d/2,WL)
plt.plot(angle,normI)

plt.title('Effects of Varying Slit Seperationg')
plt.ylabel('Normalised Intensity')
plt.xlabel('angle (radians)')
plt.savefig('varying_d.png')
plt.close()

for WL in range(550,670,50):
	normI = normalised_intensity(angle,a,d,WL)
	plt.plot(angle,normI)

plt.title('Effects of Varying Wavelength')
plt.ylabel('Normalised Intensity')
plt.xlabel('angle (radians)')
plt.savefig('varying_lambda.png')
plt.close()
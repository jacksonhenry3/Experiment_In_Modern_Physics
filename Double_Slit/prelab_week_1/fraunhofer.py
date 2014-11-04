from numpy import pi,sin,cos,arange

def normalised_intensity(angle,a,d,wave_length):
	lambdam = wave_length*10**(-9)
	c       = pi*sin(angle)/lambdam;
	alpha   = c*(a*.001);
	beta    = c*(d*.001);
	I       = ((cos(beta))**2.)*((sin(alpha))/alpha)**2.;
	return(I)
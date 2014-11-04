import numpy as np
import matplotlib.pyplot as plt

data = np.transpose(np.loadtxt('millikandata',skiprows = 3))

def q(dg,de,tg,te,V = 530):
	m = 2.04
	ve = de/te/m
	vg = dg/tg/m
	Ro = 872 #kg/m^3
	Ra = 1.2 #kg/m^2
	g = 9.81 #m/s
	eta = 1.85*10**(-5) # Ns/m^2
	r = np.sqrt(9*eta*vg/(2*(Ro-Ra)*g))
	A = .00000007776 #m
	d = 6./1000. #in (m)
	q = 6*np.pi*eta*d*r*(ve+vg)/V
	q = q/(np.sqrt((1+A/r)**3))
	return q

ne = q(.001,.001,data[1],data[0])/(1.60217657*10**(-19))

binwidth = 1/10.

plt.hist(ne,bins=np.arange(min(ne), max(ne) + binwidth, binwidth))
plt.xticks(range(14))
plt.xlabel('q/e')
plt.ylabel('Number of droplets')
plt.title('Histogram of Droplet Charges')
plt.show()
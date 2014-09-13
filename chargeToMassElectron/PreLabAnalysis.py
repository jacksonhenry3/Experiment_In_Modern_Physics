import numpy as np 
import matplotlib.pyplot as plt

# ----------- raw data and raw error ---------
currentData  = np.loadtxt('CalibrationDataCurrentVField.txt',skiprows = 1)
Current      = currentData[:,0]
Field1       = currentData[:,1]

positiondata = np.loadtxt('CallibrationDataPositionVField.txt',skiprows = 1)
Position     = positiondata[:,0]
Field2       = positiondata[:,1]

# calculate best fit line
v =  np.polyfit(Current,Field1,1)
plt.errorbar(Current,Field1,fmt = 'r.',xerr = .01, yerr = currentData[:,2])
plt.plot(Current,v[0]*Current+v[1])
plt.title("Magnetic field VS Current")
plt.xlabel("Current (A)")
plt.ylabel("Magnetic Field (Gaus)")
plt.savefig('CurrentVField.pdf')
plt.close("all")


v =  np.polyfit(Position,Field2,5)
plt.errorbar(Position,Field2,fmt = 'ro',xerr = .3,yerr = .3)
plt.plot(Position,v[0]*Position**5+v[1]*Position**4+v[2]*Position**3+v[3]*Position**2+v[4]*Position+v[5])
plt.title("Horizontal Position VS Magnetic Field")
plt.xlabel("position (cm)")
plt.ylabel("Magnetic Field (Gaus)")
plt.savefig('PositionVField.pdf')
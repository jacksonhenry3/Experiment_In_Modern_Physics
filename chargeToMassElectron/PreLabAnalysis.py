import numpy as np 
import matplotlib.pyplot as plt

# ----------- raw data and raw error ---------
currentData  = np.loadtxt('CalibrationDataCurrentVField.txt',skiprows = 1)
Current      = currentData[:,0] #Amperes
Field1       = currentData[:,1]/10 #in mili tesla

positiondata = np.loadtxt('CallibrationDataPositionVField.txt',skiprows = 1)
Position     = positiondata[:,0]
Field2       = positiondata[:,1]

# calculate best fit line
v =  np.polyfit(Current,Field1,1)
print v[0]
plt.errorbar(Current,Field1,fmt = 'r.',xerr = .01, yerr = currentData[:,2]/10)
plt.plot(Current,v[0]*Current+v[1])
plt.title("Magnetic field VS Current at Center")
plt.xlabel("Current (A)")
plt.ylabel("Magnetic Field (mT)")
plt.text(2.5,0,"slope of .78 mT/A")
plt.savefig('CurrentVField.eps')
plt.close("all")


v =  np.polyfit(Position,Field2,4)
plt.errorbar(Position,Field2,fmt = 'r.',xerr = .3,yerr = .3)
plt.plot(Position,v[0]*Position**4+v[1]*Position**3+v[2]*Position**2+v[3]*Position+v[4])
plt.title("Horizontal Position VS Magnetic Field")
plt.xlabel("Position (cm)")
plt.ylabel("Magnetic Field (Gauss)")
plt.savefig('PositionVField.eps')
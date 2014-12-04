import numpy as np
import matplotlib.pyplot as plt
data = np.transpose(np.loadtxt('noiseWeek2Data',skiprows = 1))

newCol = data[2]*10000/((600*data[1])**2)/(1000)**2

plt.loglog(data[0],newCol)
plt.xlabel("log source resistance")
plt.ylabel("log <Vj^2+Vn^2>")
plt.title("Total system noise")
plt.show()
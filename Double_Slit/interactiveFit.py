import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from  fraunhofer import *

# DSLaser = np.transpose(np.loadtxt('LaserData/DoubleSlit.txt',skiprows = 1))

DSLaser = np.transpose(np.loadtxt('BulbData/DoubleSlit.txt',skiprows = 1))


fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

def maxIndex(a):
	for i in range(len(a)):
		if a[i] == max(a):
			return(i)
angle = np.arange(-.5,.5,.00001)

a = .093
d = .4

l = 670
s = normalised_intensity(angle,a,d,l)

guess_plot, = plt.plot(angle,s,'r')
position = np.degrees((DSLaser[0]-4.88)/500)
intensity = (DSLaser[1]-99)/(np.max(DSLaser[1]))
plt.plot(position,intensity, 'b.')

plt.xlabel('angle (degrees)')
plt.ylabel('Normalized Intensity')
plt.title('Double Slit Bulb')



AsPosition = plt.axes([0.25, 0.1, 0.65, 0.03])


a = .085
d = .35
l = 670
As = Slider(AsPosition, 'l', 0, 1000, valinit=l,valfmt=u'%1.5f')
# Ds = Slider(DsPosition, 'd', 0, .5, valinit=d,valfmt=u'%1.5f')

def update(val):
    guess_plot.set_ydata(normalised_intensity(angle,a,d,As.val))
    fig.canvas.draw_idle()

As.on_changed(update)


plt.show()
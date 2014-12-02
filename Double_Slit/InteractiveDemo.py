import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from  fraunhofer import *

DSLaser = np.transpose(np.loadtxt('LaserData/DoubleSlit.txt',skiprows = 1))


fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

def maxIndex(a):
	for i in range(len(a)):
		if a[i] == max(a):
			return(i)
angle = np.arange(-.5,.5,.00001)

a = .0093
d = .041


s = normalised_intensity(angle,a,d,670)

guess_plot, = plt.plot(angle,s,'r')
position = np.degrees((DSLaser[0]-4.875)/500)
intensity = (DSLaser[1]-36)/(np.max(DSLaser[1]))
plt.plot(position,intensity, 'b.')

plt.xlabel('angle (degrees)')
plt.ylabel('Normalized Intensity')
plt.title('Double Slit Laser')



AsPosition = plt.axes([0.25, 0.1, 0.65, 0.03])
DsPosition  = plt.axes([0.25, 0.15, 0.65, 0.03])

a = .001
d = .001

As = Slider(AsPosition, 'a', 0, .002, valinit=a,valfmt=u'%1.5f')
Ds = Slider(DsPosition, 'd', 0, .01, valinit=d,valfmt=u'%1.5f')

def update(val):
    guess_plot.set_ydata(normalised_intensity(angle,As.val,Ds.val,670))
    fig.canvas.draw_idle()

As.on_changed(update)
Ds.on_changed(update)


plt.show()
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
angle = np.arange(-.08,.08,.00001)

a = .0093
d = .041


s = normalised_intensity(angle,a,d,670)

guess_plot, = plt.plot(angle,s,'r')
position  = np.arctan((DSLaser[0]-DSLaser[0][maxIndex(DSLaser[1])])/50)
intensity = (DSLaser[1]-36)/(np.max(DSLaser[1]))
plt.plot(position,intensity, 'b.')

plt.xlabel('angle')
plt.ylabel('Normalized Intensity')
plt.title('Double Slit Laser')



AsPosition = plt.axes([0.25, 0.1, 0.65, 0.03])
DsPosition  = plt.axes([0.25, 0.15, 0.65, 0.03])

a = .01
d = .04

As = Slider(AsPosition, 'a', 0, .03, valinit=a)
Ds = Slider(DsPosition, 'd', 0, .1, valinit=d)

def update(val):
    guess_plot.set_ydata(normalised_intensity(angle,As.val,Ds.val,670))
    fig.canvas.draw_idle()

As.on_changed(update)
Ds.on_changed(update)


plt.show()
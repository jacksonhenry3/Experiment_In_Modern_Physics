import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from  fraunhofer import *

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)


angle = np.arange(-.01,.01,.00001)

a = .085
d = .35


s = normalised_intensity(angle,a,d,670)

guess_plot, = plt.plot(angle,s, lw=2, color='red')

plt.plot(angle,normalised_intensity(angle,a*2,d/2,670), lw=2, color='blue')



AsPosition = plt.axes([0.25, 0.1, 0.65, 0.03])
DsPosition  = plt.axes([0.25, 0.15, 0.65, 0.03])

As = Slider(AsPosition, 'a', 0, 1, valinit=a)
Ds = Slider(DsPosition, 'd', 0, 1, valinit=d)

def update(val):
    guess_plot.set_ydata(normalised_intensity(angle,As.val,Ds.val,670))
    fig.canvas.draw_idle()

As.on_changed(update)
Ds.on_changed(update)


plt.show()

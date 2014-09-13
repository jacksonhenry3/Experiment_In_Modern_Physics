import error as er #get the error library
import numpy as np #get numpy
from sympy import Symbol,pi,sqrt #import required symbolic math components

# initialize symbols
from sympy.abc import x, y

# function to calculate error of
f    = sqrt(4*pi**2/x+y**4)

# get the error function
func =  er.getError([x,y],f,showFunc = True)

# measured values of variables and there errors
x    = np.array([.0404,.05])
dx   = np.array([.00031,.0004])
y = np.array([1,2])
dy = np.array([.1,.01])

# calculate error for each point
error = func(x,y,dx,dy)

print error
import error as er
import numpy as np

from sympy import Symbol,pi
x    = Symbol('x')
y    = Symbol('y')
dx   = Symbol('dx')
dy   = Symbol('dy')
f    = 4*pi**2/x+y**4

func =  er.getError([x,y],[dx,dy],f)
x    = np.array([.0404,.05])
dx   = np.array([.00031,.0004])
y = np.array([1,2])
dy = np.array([.1,.01])
print(func(x,y,dx,dy))
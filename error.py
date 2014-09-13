from sympy import *
from sympy.utilities.lambdify import lambdify

x = Symbol('x')
y = Symbol('y')
dx = Symbol('dx')
dy = Symbol('dy')
f = 4*pi**2/x

def getError(variables,errorVariables,func):
	FullErrorFunc = 0
	pieces = []
	for i in range(len(variables)):
		v = variables[i]
		dv = errorVariables[i]
		D = (diff(func,v)*dv)**2
		pieces.append(D)
	for piece in pieces:
		FullErrorFunc+=piece
	FullErrorFunc = sqrt(FullErrorFunc)
	variables.extend(errorVariables)
	func = lambdify(tuple(variables), FullErrorFunc ,"numpy") 
	print(FullErrorFunc)
	return(func)

import numpy as np
func =  getError([x],[dx],f)
x = np.array([.0404,.05])
dx = np.array([.00031,.0004])
from numpy import *
print(func(x,dx))

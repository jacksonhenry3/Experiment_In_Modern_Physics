from sympy import *
from sympy.utilities.lambdify import lambdify


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
	# print(FullErrorFunc)
	return(func)



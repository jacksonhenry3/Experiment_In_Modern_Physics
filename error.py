from sympy import diff,sqrt,Symbol,pprint #a symbolic math library (Computer Algebra System)
from sympy.utilities.lambdify import lambdify #allows us to make a python function from a symbolic sympy one

def getRelError(variables,func,showFunc = False):
	"""getError generates a function to calculate the error of a function. I.E. a function that
	gives you the error in its result given the error in its input. Output function is numpy ready. 
	Output function will take twice as many args as variables, one for the var and one for the error in that var.

	arguments
	variables      : a list of sympy symbols in func
	errorVariables : list of sympy ymbols representing the error in each value of variables. must be the same length as variables
	func           : a function containing your variables that you want the error of"""
	ErrorFunc = 0 # need to set function to start value
	erVars    = {}
	for i in range(len(variables)): #run through all variables in the function
		v                  = variables[i]
		dv                 =  Symbol('d'+str(v), positive = True)
		erVars['d'+str(v)] = dv
		D                  = (diff(func,v)*dv)**2
		ErrorFunc          += D

	ErrorFunc = sqrt(ErrorFunc)/func
	if showFunc:
		pprint(ErrorFunc)
		
	variables.extend(erVars.values()) #create a list of all sympy symbols involved
	func      = lambdify(tuple(variables), ErrorFunc ,"numpy") #convert ErrorFunc to a numpy rteady python lambda
	return(func)

from sympy import diff,sqrt #a symbolic math library (Computer Algebra System)
from sympy.utilities.lambdify import lambdify #allows us to make a python function from a symbolic sympy one

def getError(variables,errorVariables,func):
	"""getError generates a function to calculate the error of a function. I.E. a function that
	gives you the error in its result given the error in its input. Output function is numpy ready.

	arguments
	variables      : a list of sympy symbols in func
	errorVariables : list of sympy ymbols representing the error in each value of variables. must be the same length as variables
	func           : a function containing your variables that you want the error of"""
	ErrorFunc = 0 # need to set function to start value
	pieces        = [] #this will later contain the seperate error from each var in func
	for i in range(len(variables)): #run through all variables in the function
		v         = variables[i]
		dv        = errorVariables[i]
		D         = (diff(func,v)*dv)**2
		ErrorFunc += D

	variables.extend(errorVariables) #create a list of all sympy symbols involved
	ErrorFunc = sqrt(ErrorFunc) #this is the final formula for error
	# print(ErrorFunc) #uncomment this line to see what the error function is
	func      = lambdify(tuple(variables), ErrorFunc ,"numpy") #convert ErrorFunc to a numpy rteady python lambda
	return(func)



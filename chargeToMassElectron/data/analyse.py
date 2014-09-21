import numpy as np
import matplotlib.pyplot as plt 
import sys
sys.path.insert(0, '../../')

data  = np.loadtxt('data.txt',skiprows = 1)
voltage = data[:,0]
current= data[:,1]
diameter = data[:,2]
diameterErr = np.ones(len(diameter))*.4
voltageErr = np.ones(len(voltage))*.5
voltageErr[-1] = 5
voltageErr[-2] = 5
voltageErr[-3] = 5
voltageErr[-4] = 5

currentError = np.ones(len(current))*.05
rootVByI = np.sqrt(voltage)/current
rootVByIErr = np.sqrt(voltageErr**2/(4*current**2*voltage)+voltage*currentError**2/(current**4))

# a      =  np.expand_dims(,axis = 1)
dat = np.transpose(np.array([voltage,voltageErr,current,currentError,diameter,diameterErr,rootVByI,rootVByIErr]))
np.savetxt('finalColumnData.txt',dat,fmt = '%.2e' )



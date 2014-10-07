import numpy as np 
import matplotlib.pyplot as plt 

#get the data, dont look at the column labels, transpose it in to columnar data
data = np.transpose(np.loadtxt("2filterGainData.txt",skiprows = 1))
freq = data[0] #in kHz
channel1 = data[1] #in Volts
channel2 = data[2] #in Volts
channel1_err = data[3] #in Volts
channel2_err = data[3] #in Volts

gain = channel2/channel1 #the change in signal value
rel_gain_err = channel2_err/channel2 #the relative error in the gain

#to whoever is reading this. Im sorry about this line. Its just to make sure all the data can be put in to a single array.
calculated_Data_columns = np.transpose(np.append(np.append(data,np.expand_dims(gain,axis = 0) ,0),np.expand_dims(rel_gain_err,axis = 0),0))

#the header to the data file
header = "frequency (kHz)	Channel 1 (V)	Channel2 (V)	Channel 1 error (V)		channel2 error (V)	gain 	relative gain error"
np.savetxt('dataCalc.txt',calculated_Data_columns,newline = '\n', delimiter  = '	', fmt = '%.2e'  ,header = header)

#set up for a log log plot
plt.subplot(111, xscale="log", yscale="log") 
plt.errorbar(freq, gain, yerr=rel_gain_err*gain,fmt = 'r--')  
plt.show() 
import numpy as np 
import matplotlib.pyplot as plt 
data = np.transpose(np.loadtxt("2filterGainData.txt",skiprows = 1))
freq = data[0] #in kHz
channel1 = data[1]
channel2 = data[2]
channel1_err = data[3]
channel2_err = data[3]

gain = channel2/channel1
rel_gain_err = channel2_err/channel2

gain = np.expand_dims(gain,axis = 0)
rel_gain_err = np.expand_dims(rel_gain_err,axis = 0)
header = "frequency (kHz)	Channel 1 (V)	Channel2 (V)	Channel 1 error (V)	channel2 error (V)	gain 	relative gain error"
np.savetxt('dataCalc.txt',np.transpose(np.append(np.append(data,gain,0),rel_gain_err,0)),newline = '\n', delimiter  = '	', fmt = '%.2e'  ,header = header  )
# plt.loglog(data[0],data[2]/data[1],'r')

# plt.show()
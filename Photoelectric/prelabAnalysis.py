import numpy as np 
import matplotlib.pyplot as plt 

data = np.transpose(np.loadtxt("prelabData.txt",skiprows = 2)) #get the data and put it in apropriat columns
voltage = data[0]
current = data[1]

#taking a numerical derivative 
def num_div(vals,dists):
	div = []
	for i in range(len(vals)-1):
		a = (vals[i+1]-vals[i])/(dists[i+1]-dists[i])
		div.append(a)  #add the discrete difference bettwen two succesive points
	return(div)


def get_tangents(vals,dists):
	vals = np.sort(vals) #sort all the values
	dists = np.sort(dists)
	neg = -100 #start at arbitrary values and find the value closest to zero that is either negative or positive
	pos = 100 
	for v in range(len(vals)):
		if vals[v]<=0 and vals[v]>neg:
			neg = vals[v] 
			negi = v
		if vals[v]>=0 and vals[v]<pos:
			pos = vals[v]
			posi = v

	tangent1_Slope = (neg-vals[0])/(dists[negi]-dists[0])
	tangent2_Slope = (pos-vals[-1])/(dists[posi]-dists[-1])

	b = vals[posi]-tangent2_Slope*dists[posi]

	return ([tangent1_Slope,vals[0]],[tangent2_Slope,b])





currentediv = num_div(current,voltage)

tan1 =  get_tangents(current,voltage)[0]
tan2 =  get_tangents(current,voltage)[1]

x = (tan2[1]-tan1[1])/(tan1[0]-tan2[0])


plt.plot(voltage,tan1[0]*voltage+tan1[1])
plt.plot(voltage,tan2[0]*voltage+tan2[1])

plt.plot(voltage,current,'b.')
plt.plot(voltage[0:-1],currentediv,'r.')

plt.show()
import numpy as np 
import matplotlib.pyplot as plt 

data = np.sort(np.transpose(np.loadtxt("prelabData.txt",skiprows = 2)),axis = 1) #get the data and put it in apropriat columns
data = np.sort(np.transpose(np.loadtxt("yellow.txt")),axis = 1) #get the data and put it in apropriat columns
voltage = data[0]
current = data[1]

#function to take a numerical derivative via finite difference method
def num_div(vals,dists):
	div = [] #will contain succesive differences in points
	for i in range(len(vals)-1):#loop over 
		a = (vals[i+1]-vals[i])/(dists[i+1]-dists[i]) #the difference in values over the difference in distances
		div.append(a)  #add the discrete difference bettwen two succesive points
	return(div)


def get_tangents(vals,dists): #gets aproximate tangant line by crude linear aproximation
	""" gets two tangents of two section of data. The first one is the line through the first point and 
	the point closest to zero that is still negative while the second line is the line through the last data point and
	the smallest positive value.
	"""
	neg = -100 #start at arbitrary values and iterate to find the value closest to zero that is either negative or positive
	pos = 100 
	for i in range(len(vals)): #iterate over all vals and dists
		if vals[i]<=0 and vals[i]>neg:
			neg = vals[i] 
			negi = i
		if vals[i]>=0 and vals[i]<pos:
			pos = vals[i]
			posi = i

	tangent1_Slope = (neg-vals[0])/(dists[negi]-dists[0])
	tangent2_Slope = (pos-vals[-1])/(dists[posi]-dists[-1])



	b2 = vals[posi]-tangent2_Slope*dists[posi]
	b1 = vals[negi]-tangent1_Slope*dists[negi]
	x = (b1-b2)/(tangent2_Slope-tangent1_Slope)
	return ([tangent1_Slope,b1],[tangent2_Slope,b2],x)





currentediv = num_div(current,voltage)

[tan1,tan2,x] =  get_tangents(current,voltage)

x = (tan2[1]-tan1[1])/(tan1[0]-tan2[0])
print x

plt.plot(voltage,tan1[0]*voltage+tan1[1])
plt.plot(voltage,tan2[0]*voltage+tan2[1])

plt.plot(voltage,current,'b.')
plt.plot(voltage[0:-1],currentediv,'r.')

plt.show()
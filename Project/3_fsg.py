import numpy as np
from pandas import *
import math

# a = np.arange(9).reshape((3,3))
arr = np.loadtxt(open("csv files/matlab.csv","rb"),delimiter=",",skiprows=0)
data = np.loadtxt(open("csv files/output_tindex.csv","rb"),delimiter=",",skiprows=0)

# slice the arr(matlab csv) with the start time and end time
# then drop the duplicates from the ndarray using panda
# array = DataFrame(arr[:,2:]).drop_duplicates().values
# print len(array)
array = np.loadtxt(open("csv files/groupinfo.csv","rb"),delimiter=",",skiprows=0)

def distanceDelta(x,t):
	dist4=10000
	ndarray=np.array([element for element in arr if element[3] == t])
	for l in ndarray:
		if math.hypot(x[0]-l[0], x[1]-l[1]) < dist4:
			dist4 = math.hypot(x[0]-l[0], x[1]-l[1])
	return dist4
	# return [x[2],t,dist4,math.exp(-theta3/dist4**2)]

# a=[x,y,frame,pede]
# b=[x,y,start,end]
# c=[0,20,40]
def fsg(Data,theta3,theta4):

	theta3 = 0.5
	theta4 = 0.01
	output3 = []
	
	for a in Data:
		for b in array:
			if a[2] in range(int(b[0]),int(b[1])+1):
				distance = distanceDelta(a,b[1])
				if distance == 0 and 10000:
					output3.append([a[2],a[3],b[1],distance,1]) #[a[2],a[3],b[1],distance,1]
					print [a[2],a[3],b[1],distance,1]
				else:
					output3.append([a[2],a[3],b[1],distance,math.exp(-theta3/distance**2)])
					print [a[2],a[3],b[1],distance,math.exp(-theta3/distance**2)]
					# [frame,pedestrian index,stationary group index,distance,exp]

	# np.savetxt('csv files/4_fsgoutput.csv', output3, delimiter = ',')

fsg(data,0.5,0)
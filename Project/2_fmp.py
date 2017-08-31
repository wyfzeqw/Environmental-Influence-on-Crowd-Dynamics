import numpy as np
import math

data_frame = np.loadtxt(open("csv files/demo_tindex.csv","rb"),delimiter=",",skiprows=0)
data_pedestrian = np.loadtxt(open("csv files/demo_pindex.csv","rb"),delimiter=",",skiprows=0)

# def compareList(a,b):
# 	# add the value of two lists into the relavant tmp list
# 	tmp1,tmp2 = a[:],b[:]
# 	# the np.all() function is to solve the problem of ValueError: 
# 	# The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
# 	if np.all(tmp1) == np.all(tmp2):
# 		return 1
# 	else:
# 		return 0

def preList(a,M):
	for line in M:
		if a[2] == line[2]+20 and a[3] == line[3]:
			return line
	return a

def nextFramePedestrian(m, D):
	for n in range(len(D)):
		if m[2]==D[n][2]-20 and m[3]==D[n][3]:
			return D[n] # get the next list
	# if the range is out of the frame, it is assume as the same direction and speed so the axis is (2x2-x1, 2y2-x2)
	pre=preList(m,data_pedestrian)
	return [m[0]*2-pre[0], m[1]*2-pre[1], 99.0, m[3]]

# print nextFramePedestrian([1793,571,700,1], data_pedestrian)
# print nextFramePedestrian([525,122,0,1], data_pedestrian)
# [525,122,0,1], [1793,571,700,1]
# => correct

def dist2(m1,m2):
	m3 = nextFramePedestrian(m2,data_pedestrian)
	d1 = math.hypot(m1[0]-m2[0],m1[1]-m2[1])
	d2 = math.hypot(m1[0]-m3[0],m1[1]-m3[1])
	d3 = math.hypot(m2[0]-m3[0],m2[1]-m3[1])
	dist2 = (d1+d2)**2 - d3**2
	return dist2

# print dist2([525,122,0,1],[597,148,0,3]) => correct

def fmp(d):
	theta2 = 0.02
	para = d[0][:]
	output = []
	for k in d[1:]:
		if k[2] == para[2]:
			dist = dist2(para,k)
			if dist != 0:
				output.append([k[2], dist, math.exp(-theta2/dist)])
			else:
				output.append([k[2], dist, 1])
		else:
			para = k
	np.savetxt('output.csv', output, delimiter = ',')
	print '------output success------'
	return 0

fmp(data_frame)







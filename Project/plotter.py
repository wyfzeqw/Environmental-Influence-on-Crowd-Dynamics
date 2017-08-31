import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt(open("csv files/GT_T_009991.csv","rb"),delimiter=",",skiprows=0)

# arr=[[1,3],[1,2],[2,3],[1,4]]
arr=[]

for a in range(len(data)):
	for b in range(len(data[a])):
		if data[a][b] !=0:
				arr.append([a+1,b+1,data[a][b]])

# print arr

for x in arr:
	if x[2] == 2880:
		plt.scatter(x[0],x[1])
		print "scatter success: %d" % (x[0])

plt.show()
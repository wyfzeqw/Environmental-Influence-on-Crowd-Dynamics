import math
import matplotlib.pyplot as plt
import numpy as np

# the pedestrian walking path dataset saved as my_data
my_data = np.loadtxt(open("csv files/output_tindex.csv","rb"),delimiter=",",skiprows=0)

# distanceAlpha function is used to calculate the shortest distance from x to the obstacle set.
# input [x,y,....] output distance
def distanceAlpha(matrix):

	obstacle = [[894,586],[1652,481],[1800,767],[1540,269],[1420,125],[247,447],[89,791],[69,466]]
	dist1 = 10000
	
	for line in range(len(obstacle)):
		if math.hypot(matrix[0]-obstacle[line][0], matrix[1]-obstacle[line][1]) < dist1:
			dist1 = math.hypot(matrix[0]-obstacle[line][0], matrix[1]-obstacle[line][1])

	return dist1

# print 0.0
# print obst([525,122,0,1])

def fsl(Data):

	expower = 1
	theta1 = 0.01
	output1 = []

	for line in Data:
		distance = distanceAlpha(line)
		if distance != 0:
			# [line[2],line[3],distance,math.exp(-theta1/distance**2)]
			exp = math.exp(-theta1/distance**2)
			expower*=exp
			output1.append([line[2],line[3],distance,exp])
			print [line[2],line[3],distance,exp]

	# np.savetxt('csv files/1_fsloutput.csv', output1, delimiter=',')
	print "csv file written successfully!"
	print expower


fsl(my_data)



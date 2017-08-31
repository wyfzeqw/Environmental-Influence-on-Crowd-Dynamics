import os
import math
import matplotlib.pyplot as plt
import numpy as np

# read all the txt files in the Annotation and load them to the array
arr = []
path = "Anno"
files = os.listdir(path)
for file in files:
	if not os.path.isdir(file):
		f = open(path+"/"+file)
		f = np.loadtxt(f)
		f = f.reshape(-1, 3)
		arr.extend(f)


# save the array to csv files by pedestrian sequence
np.savetxt('demo_pindex.csv', arr, delimiter = ',')  

# sort the array by time index
# and then save the array to csv files
arr.sort(key=lambda x:x[2])
np.savetxt('demo_tindex.csv', arr, delimiter = ',')  


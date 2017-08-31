import numpy as np
import matplotlib.pyplot as plt

x = np.loadtxt(open("csv files/emap.csv","rb"),delimiter=",",skiprows=0)
nrows, ncols = 1080, 1920
z = x.reshape((nrows, ncols))
z_min, z_max = -np.abs(z).max(), np.abs(z).max()
v=[[x,1] for x in range(1,1920)]
v=np.asarray(v)
plt.imshow(z,cmap='jet')
plt.title('Scene Layout Map')
# plt.colorbar()
# plt.scatter(v[:,0],v[:,1],c='b')
plt.show()
import numpy as np
from gd import *
from mu import *
# training set
x = np.loadtxt(open("csv files/demo_tindex.csv","rb"),delimiter=",",skiprows=0)
# learning rate
eta = 0.001
# max iteration threshold
max_itor = 1000
# the residuals of four parameters
diff=[0,0,0,0]
# Iteration threshold stops the iteration 
# when the difference between the two iterations of 
# the loss function is less than the threshold
epsilon = 0.01
# calculate the cost function
error1 = 0
error0 = 0
count the iteration
cnt = 0
# initial parameters
theta1 = 0.01
theta2 = 0.02
theta3 = 0.5
theta4 = 0.0

# diffunc() used to calculate the diff of four parameters
def diffunc(theta1,theta2,theta3,theta4):
    sx1,sx2,sx3,sx4=0.0,0.0,0.0,0.0
    px1,px2,px3,px4=0.0,0.0,0.0,0.0
    summu=zeltafunc(theta1,theta2,theta3,theta4)
    
    for i in range(len(x)):
        prob=mufuct(x[i],theta[0],theta[1],theta[2],theta[3])/summu
        sx1+=fsldiff(x[i])
        sx2+=fmpdiff(x[i])
        sx3+=fsgdiff3(x[i],theta4)
        sx4+=fsgdiff4(x[i],theta3,theta4)
        px1+=fsldiff(x[i])*prob
        px2+=fmpdiff(x[i])*prob
        px3+=fsgdiff3(x[i],theta4)*prob
        px4+=fsgdiff4(x[i],theta3,theta4)*prob
    
    return [sx1-px1, sx2-px2, sx3-px3, sx4-sx4]
        
while True:
    cnt+=1
    # iteration of parameter
    for i in range(len(x)):
        diff = diffunc(theta1,theta2,theta3,theta4)
        theta1 -= eta * diff[0]
        theta2 -= eta * diff[1]
        theta3 -= eta * diff[2]
        theta4 -= eta * diff[3]
    
    # calculate the cost function
    error1=0
    for l in range(len(x)):  
        error1 += abs(math.log(mufuct(x[l],theta[0],theta[1],theta[2],theta[3]))-math.log(summu))
    if abs(error1-error0) < epsilon:
        break
    else:
        error0 = error1
    print 'theta1 : %f, theta2 : %f, theta3 : %f, theta4 : %f, cost : %f' % (theta1, theta2, theta3, theta4, error1)
print 'Okay: theta1 : %f, theta2 : %f, theta3 : %f, theta4 : %f' % (theta1, theta2, theta3, theta4)
print 'Iteration time: %d' % (cnt)
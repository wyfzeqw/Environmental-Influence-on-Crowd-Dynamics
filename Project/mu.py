import numpy as np
import math

arr = np.loadtxt(open("csv files/matlab.csv","rb"),delimiter=",",skiprows=0)
data = np.loadtxt(open("csv files/output_tindex.csv","rb"),delimiter=",",skiprows=0)
array = np.loadtxt(open("csv files/groupin.csv","rb"),delimiter=",",skiprows=0)

a = [[x+1,y+1] for y in range(500,700) for x in range(725,1075)]
b = [[x+1,y+1] for y in range(226) for x in range(1920)]
c = [[x+1,y+1] for y in range(226,1080) for x in range(int(444-0.5*(y-226)))]
d = [[x+1,y+1] for y in range(226,1036) for x in range(int(1465+(9./16)*(y-226)),1920)]

def fslexp(x,theta1):
    
    obstacle = a+b+c+d
    dist1 = 10000
    for line in range(len(obstacle)):
        if math.hypot(x[0]-obstacle[line][0], x[1]-obstacle[line][1]) < dist1:
            dist1 = math.hypot(x[0]-obstacle[line][0], x[1]-obstacle[line][1])
            fraction = -theta1/dist1 if dist1 !=0 else 0
    return math.exp(fraction)

def distanceTwo(x,line):
    for l in data:
        if l[3] == line[3] and l[2] == line[2]+20:
            dist2 = (math.hypot(x[0]-line[0],x[1]-line[1])+math.hypot(x[0]-l[0],x[1]-l[1]))**2-math.hypot(line[0]-l[0],line[1]-l[1])**2
        else:
            dist2 = 4*(math.hypot(x[0]-line[0],x[1]-line[1])**2)
    return dist2

def fmpexp(x,theta2): 
    fractsum=0
    for line in data:
        if line[2]==x[2]:
            dist2=distanceTwo(x,line)
            fraction = -theta2/dist2 if dist2 !=0 else 0
            fractsum+=fraction
    return math.exp(fractsum)

def distanceDelta(x,t):
    dist4=10000
    ndarray=np.array([element for element in arr if element[3] == t])
    for l in ndarray:
        if math.hypot(x[0]-l[0], x[1]-l[1]) < dist4:
            dist4 = math.hypot(x[0]-l[0], x[1]-l[1])
    return dist4

def fsgexp(x, theta3, theta4):
    fractsum=0
    for arr in array:
        if arr[1] != (330 or 9990 or 20160 or 50090 or 70160):
            if x[2] in range(int(arr[0]),int(arr[1])+1):
                fraction = -theta3/(distanceDelta(x,arr[1])+theta4*arr[2])
                fractsum+=fraction
    return math.exp(fractsum)

def mufuct(x,theta1,theta2,theta3,theta4):
    return fslexp(x,theta1)*fmpexp(x,theta2)*fsgexp(x, theta3, theta4)

def zeltafunc(theta1,theta2,theta3,theta4):
    summu=0
    for i in data:
        mu = mufuct(i,theta1,theta2,theta3,theta4)
        summu+=mu
    return summu


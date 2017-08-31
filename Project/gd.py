import numpy as np
import math

arr = np.loadtxt(open("csv files/matlab.csv","rb"),delimiter=",",skiprows=0)
data = np.loadtxt(open("csv files/input_tindex.csv","rb"),delimiter=",",skiprows=0)
array = np.loadtxt(open("csv files/groupin.csv","rb"),delimiter=",",skiprows=0)

def fsldiff(x):
    obstacle = [[894,586],[1652,481],[1800,767],[1540,269],[1420,125],[247,447],[89,791],[69,466]]
    dist1 = 10000
    for line in range(len(obstacle)):
        if math.hypot(x[0]-obstacle[line][0], x[1]-obstacle[line][1]) < dist1:
            dist1 = math.hypot(x[0]-obstacle[line][0], x[1]-obstacle[line][1])
            fraction = -1/dist1
    return fraction

def distanceAlpha(x,line):
    for l in data:
        if l[3] == line[3] and l[2] == line[2]+20:
            dist2 = (math.hypot(x[0]-line[0],x[1]-line[1])+math.hypot(x[0]-l[0],x[1]-l[1]))**2-math.hypot(line[0]-l[0],line[1]-l[1])**2
        else:
            dist2 = 4*(math.hypot(x[0]-line[0],x[1]-line[1])**2)
    return dist2

def fmpdiff(x): 
    fractsum=0
    for line in data:
        if line[2]==x[2]:
            dist2=distanceAlpha(x,line)
            fraction = -1/dist2 if dist2 !=0 else 0
            fractsum+=fraction
    return fractsum

def distanceBeta(x,t):
    dist4=10000
    ndarray=np.array([element for element in arr if element[3] == t])
    for l in ndarray:
        if math.hypot(x[0]-l[0], x[1]-l[1]) < dist4:
            dist4 = math.hypot(x[0]-l[0], x[1]-l[1])
    return dist4

def fsgdiff3(x,theta4):
    fractsum1=0
    for arr in array:
        if arr[1] != (330 or 9990 or 20160 or 50090 or 70160):
            if x[2] in range(int(arr[0]),int(arr[1])+1):
                fraction1 = -1/(distanceBeta(x,arr[1])+theta4*arr[2])
                fractsum1+=fraction1
    return fractsum1

def fsgdiff4(x,theta3,theta4):
    fractsum2=0
    for arr in array:
        if arr[1] != (330 or 9990 or 20160 or 50090 or 70160):
            if x[2] in range(int(arr[0]),int(arr[1])+1):
                fraction2 = theta3*arr[2]/(distanceBeta(x,arr[1])+theta4*arr[2])**2
                fractsum2+=fraction2
    return fractsum2
import numpy as np
path="/home/ys/pychon_code/ML_Yan_2/day0823/KNN_ShouXie/trainingDigits/0_0.txt"
f = open(path, "r")
reList = [0]*1024
for i in range(32):
    linestr = f.readline()
    for j in range(32):
        #print linestr[j]
        reList[i * 32 + j] = float(linestr[j])
print np.array(reList)
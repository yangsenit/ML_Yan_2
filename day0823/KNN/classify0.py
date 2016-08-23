# -*- coding: utf-8 -*-
import numpy as np
import operator
import time
#这里的inx 是 np类型array  dataset是np类型的array lables list k为int类型
def classify0(inX,dataSet,labels,k):
    dataSetSize=dataSet.shape[0]   #array
    diffMat=np.tile(inX,(dataSetSize,1))-dataSet   #array
    sqDiffMat=diffMat**2  #array
    sqDistances=sqDiffMat.sum(axis=1) #按行求和
    distances=sqDistances**0.5
    sortedDistIndicies=distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel=labels[sortedDistIndicies[i]]
        classCount[voteIlabel]=classCount.get(voteIlabel,0)+1 # 如果字典没有获得相应的值，就用字典0作为值返回
    sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def createData():
    dataList0=[]
    dataList1=[]
    dataList2=[]
    lables=[]
    for i in range(100):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        dataList1.append([x,y])
    for i in range(100):
        x = np.random.uniform(1, 2)
        y = np.random.uniform(1, 2)
        dataList2.append([x, y])
    dataList0.extend(dataList1)
    dataList0.extend(dataList2)
    for i in range(200):
        if i<100:
            lables.append(0)
        else:
            lables.append(1)
    return np.array(dataList0),lables
dataSet,lables =createData()
print dataSet
print lables
start=time.time()
r=classify0(np.array([2,2]),dataSet,lables,10)
end=time.time()
print r,end-start


# -*- coding:utf-8 -*-
import numpy as np
import day0823.KNN.classify0 as knn
from os import listdir
#path="/home/ys/pychon_code/ML_Yan_2/Util"
#print listdir(path)
path="/home/ys/pychon_code/ML_Yan_2/day0823/KNN_ShouXie/trainingDigits"
#print listdir(path)
def img2vector(path):
    f=open(path,"r")
    reList=[0.0]*1024
    for i in range(32):
        linestr=f.readline()
        for j in range(32):
            reList[i*32+j]=float(linestr[j])
    return np.array(reList)

def handwritingClassTest():
    hwLabel=[]
    trainingFileList=listdir(path)
    m=len(trainingFileList)
    trainMat=np.zeros((m,1024))
    for i in range(m):
        fileNameStr=trainingFileList[i]
        fileStr=fileNameStr.split(".")[0]
        classNumStr=int(fileStr.split("_")[0])
        hwLabel.append(classNumStr)
        # 非常具有学习的价值，动态字符串的拼接
        trainMat[i,:]=img2vector("/home/ys/pychon_code/ML_Yan_2/day0823/KNN_ShouXie/trainingDigits/%s" %fileNameStr)
    testFileList=listdir("/home/ys/pychon_code/ML_Yan_2/day0823/KNN_ShouXie/testDigits")
    errorCount=0.0
    mTest=len(testFileList)
    for i in range(mTest):
        fileNameStr=testFileList[i]
        fileStr=fileNameStr.split(".")[0]
        classNumStr=int(fileStr.split("_")[0])
        vectorUnderTest=img2vector("/home/ys/pychon_code/ML_Yan_2/day0823/KNN_ShouXie/testDigits/%s" %fileNameStr)
        classifierResult=knn.classify0(vectorUnderTest,trainMat,hwLabel,3)
        print "the classifier came back with : %d,the real answer is:%d" %(classifierResult,classNumStr)
        if(classifierResult!=classNumStr):
            errorCount+=1.0
    print "\n the total number of errors is :%d" %errorCount
    print "\n the total error rate is :%f" %(errorCount/float(mTest))

handwritingClassTest()
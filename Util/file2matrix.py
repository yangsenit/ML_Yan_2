# -*- coding:utf-8 -*-
import numpy as np
'''
    我们假设文本数据的格式为

    1,2,3,0
    4,5,6,1
    前三列是数据
    后三列是标签
    file2matrix 要返回的值有  数据以np.array返回 标签以list返回
'''
def file2matrix(filename):
    f=open(filename,"r")
    lines=f.readlines()
    numberOfLines=len(lines)
    returnMatrix=np.zeros((numberOfLines,3))
    #print returnMatrix
    label=[]
    for line in lines:
        index=0
        line=line.strip()
        listFromLine=line.split(",")
        returnMatrix[index,:]=listFromLine[0:3]
        label.append(int(listFromLine[3]))
        index+=1
    return returnMatrix,label

path="/home/ys/pychon_code/ML_Yan_2/data/1.txt"
x,y=file2matrix(path)
print x
print type(x)
print y
print type(y)




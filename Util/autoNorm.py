# -*- coding:utf-8 -*-
import numpy as np
'''
 归一化的操作
 newValue=(oldvalue-min)/(max-min) 归一话到（0,1）
'''
def autoNorm(dataSet):  #对m行n列数据归一化
    m=np.shape(dataSet)[0]
    minval=dataSet.min(0)  #所有列的最小值全部放在 minval minval是array
    maxval=dataSet.max(0)
    ranges=maxval-minval
    normDataSet = np.zeros(np.shape(dataSet))
    normDataSet=dataSet-np.tile(minval,(m,1))
    normDataSet=normDataSet/np.tile(ranges,(m,1))
    return normDataSet,ranges,minval
dataSet=np.array([[1,2,3,4],[6,7,8,9],[10,11,12,13]],dtype=float)
print dataSet
print autoNorm(dataSet)
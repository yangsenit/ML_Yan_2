# -*- coding: utf-8 -*-
import numpy as np
x1=np.random.rand(4,4)
print x1
print type(x1)  #<type 'numpy.ndarray'>
x2=np.mat(x1)
print x2
print type(x2) #<class 'numpy.matrixlib.defmatrix.matrix'>
x3=np.matrix(x1)
print x3
print type(x3) #<class 'numpy.matrixlib.defmatrix.matrix'>
x4=x3.I
print x4
print type(x4)

x5=x3*x4   #这里已经是两个矩阵相乘
print x5
print type(x5)

print type(np.eye(4))
x6=x5-np.eye(4)
print x6
print type(x6)




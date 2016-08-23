# -*- coding: utf-8 -*-
import numpy as np
import operator
x=np.array(
    [[1,2],
    [3,4]]
)
r=x.sum(axis=0) #0 是 按列   1 是按行
print r


print "*******************"

x1=np.array([1,3,2])
print x1
print type(x1)
print x1.argsort()



x2={1:'a',3:'c',2:'b'}
#r=sorted(x2.iteritems(),reverse=False)
r=sorted(x2.iteritems(),key=operator.itemgetter(0),reverse=False)   #is a function not a array
#r=sorted(x2.iteritems(),key=lambda s:s[0],reverse=False)
print x2
print r


# list 遇到 np.array()怎么处理
a=[1,2,3]
b=np.array([4,5,6])
r=a+b
print a ,type(a)
print b ,type(b)
print r ,type(r)
import numpy as np
s="sdfsj sadf a sa fsd f a"
s=s.strip()
r=s.split(" ")
print r
print type(r)
#['sdfsj', 'sadf', 'a', 'sa', 'fsd', 'f', 'a']
#<type 'list'>
x=np.array([[1,2,3],[4,5,6]])
print x[:,:]
print x[:,1]
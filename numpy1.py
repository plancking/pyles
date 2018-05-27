import numpy as np

a=np.arange(24)
print(a)

'''
b=a.reshape((4,6))
print(a)
print(b)#不改变a
c=a.resize((4,6))
print(a)
'''
a.resize((4,6))#直接改变a
'''
b=a.swapaxes(0,1)#转置，不改变a
print(a)
print(b)
'''
'''
b=a.flatten()#降维，不改变a
print(a)
print(b)
'''
'''
b=a.astype(np.float)#重新创建一个np.type型的数组，不改变a
print(a)
print(b)
'''
#print(a.tolist())

b=np.arange(24)
b.resize((4,6))
c=np.concatenate((a,b))
print(c)

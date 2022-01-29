import numpy as np

A=np.array(list(map(float,input().split())))
print(np.floor(A),np.ceil(A),np.rint(A),sep='\n')
import numpy as np

n,m=map(int,input().split())

a=[list(map(int,input().split())) for i in range(n)]
print(np.prod(np.sum(a,axis=0),None))
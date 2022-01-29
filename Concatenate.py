import numpy as np

n,m,p=map(int,input().split())

l1=[list(map(int,input().split())) for i in range(n)]
l2=[list(map(int,input().split())) for i in range(m)]
a1=np.array(l1)
a2=np.array(l2)

print(np.concatenate((a1,a2),axis=0))
import numpy as np

n,m=map(int,input().split())

l=[list(map(int,input().split())) for i in range(n)]

a=np.array(l)

print(max(np.min(a,axis=1)))
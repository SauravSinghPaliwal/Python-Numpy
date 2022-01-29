import numpy as np

c=list(map(float,input().split()))
x=float(input())

print(np.polyval(c,x))
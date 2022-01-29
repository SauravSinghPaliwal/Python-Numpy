import numpy as np
n, m = map(int, input().split())

a = np.array([input().strip().split() for _ in range(n)], int)
print (a.transpose())
print (a.flatten())
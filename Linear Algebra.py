import numpy as np

A = int(input())
B = np.array([input().split() for _ in range(A)], float)
print(np.linalg.det(B))
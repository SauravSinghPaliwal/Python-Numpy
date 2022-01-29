import numpy as np

a, b = [int(x) for x in input().strip().split()]

print(np.eye(a, b))
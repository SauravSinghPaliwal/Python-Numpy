import numpy as np

N,M = map(int, input().split())
l = []

for i in range(N):
    a = list(map(int, input().split()))
    l.append(a)

l = np.array(l)

np.set_printoptions(legacy='1.13')
print(np.mean(l, axis = 1))
print(np.var(l, axis = 0))
print(np.std(l))
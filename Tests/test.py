import numpy as np

a = np.zeros((4,4))

for i in range(0,4):
    for j in range(0, 4):
         a[i][j] = i+j

b = np.max(a,axis=1)
c = a[:,3]
print(a)
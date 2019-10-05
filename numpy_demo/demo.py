import numpy as np

a = np.array([1,2,3,4])
b = [2,4,6,8]
c = a[a > 1]
d = c[0]
print(b[d])
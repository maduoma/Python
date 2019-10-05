import numpy as np 
import scipy as sp
import matplotlib.pylab as plt

a = np.array([1,2,3,4])
b = [2,4,6,8]
c = a[a > 1]
d = c[0]
print(b[d])

# Now, open a cmd window like before. Use the next set of commands to install NumPy, SciPy and Matplotlib:
# python -m pip install numpy
# python -m pip install scipy
# python -m pip install matplotlib
t = sp.linspace(0, 1, 100)
plt.plot(t, t**2)
plt.show()
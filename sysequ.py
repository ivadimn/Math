import numpy as np

M = np.array([[3., -2., 5],
              [7., 4.,-8.],
              [5., -3., -4.]])
print(M)
v = np.array([7., 3., -12.])

v1 = np.linalg.solve(M, v)
print(v1)
M[1] = M[1] * 2
print(M[1])
import numpy as np
P = np.random.random((100, 2))
x, y = P[:, 0], P[:, 1]
D = np.sqrt((x - x[:, None]) ** 2 + (y - y[:, None]) ** 2)
print("first 5x5 block:\n", D[:5, :5])
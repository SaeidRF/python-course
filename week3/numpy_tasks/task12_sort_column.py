import numpy as np
Z = np.random.randint(0, 10, (3, 3))
print("original:\n", Z)
n = 1
print("\nSorted array by column", n, ":\n", Z[Z[:, n].argsort()])
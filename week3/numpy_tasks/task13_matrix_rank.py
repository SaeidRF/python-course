import numpy as np
matrix = np.random.rand(4, 4)
print("matrix:\n", matrix)
rank = np.linalg.matrix_rank(matrix)
print("matrix rank:", rank)
import numpy as np
matrix = np.random.rand(3, 3)
print("Matrix:\n", matrix)
row_means = matrix.mean(axis=1, keepdims=True)
result = matrix - row_means
print("\nMatrix after subtracting row means:\n", result)
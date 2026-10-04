import numpy as np
matrix = np.random.random((5, 5))
m_min = matrix.min()
m_max = matrix.max()
normalized_matrix = (matrix - m_min) / (m_max - m_min)
print("normalized matrix:\n", normalized_matrix)
import numpy as np
Z = np.arange(256).reshape(16, 16)
block_sum = Z.reshape(4, 4, 4, 4).sum(axis=(1, 3))
print("original shape:", Z.shape)
print("block sum shape:", block_sum.shape)
print("Block sums:\n", block_sum)
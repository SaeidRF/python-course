import numpy as np
Z = np.random.uniform(0, 10, 10)
print("random array:", Z)
print("1 floor:", np.floor(Z))
print("2 astype:", Z.astype(int))
print("3 trunc:", np.trunc(Z))
print("4 floor:", Z - Z % 1)
print("5 ceil-1:", np.ceil(Z) - 1)
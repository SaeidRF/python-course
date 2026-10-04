import numpy as np
X = np.random.randint(0, 2, 5)
Y = np.random.randint(0, 2, 5)
print("X=", X, " Y=", Y)
print("np.array_equal:", np.array_equal(X, Y))
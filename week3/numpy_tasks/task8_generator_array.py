import numpy as np
def generate():
    for x in range(10):
        yield x
G = np.fromiter(generate(), dtype=int)
print(G)
import numpy as np
S = np.zeros(5,dtype=[("position", [("x", float), ("y", float)]),("color", [("r", np.ubyte), ("g", np.ubyte), ("b", np.ubyte)])],)
S["position"]["x"] = np.random.random(5)
S["position"]["y"] = np.random.random(5)
S["color"]["r"] = np.random.randint(0, 256, 5)
S["color"]["g"] = np.random.randint(0, 256, 5)
S["color"]["b"] = np.random.randint(0, 256, 5)
print(S)

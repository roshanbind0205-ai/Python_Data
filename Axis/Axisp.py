import numpy as np

marks = np.array([
    [80, 85, 90],
    [70, 75, 65],
    [92, 88, 95]
])
print(np.mean(marks, axis=0))
print(np.mean(marks, axis=1))

# argpartition()
import numpy as np
x = np.array([11, 10, 15, 1, 0, 7, 8, 6, 9, 15, 16, 5, 4, 6, 0])
index_val = np.argpartition(x, -4)[-4:]
print(np.sort(x[index_val]))

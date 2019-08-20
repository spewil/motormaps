import numpy as np
from matplotlib import pyplot as plt
import matplotlib

matplotlib.use("TkAgg")

# A problem with a low condition number is said to be well-conditioned, while a problem with a high condition number is said to be ill-conditioned.

size = 5
conds = []
for _ in range(1000):
    A = np.random.normal(size=(size, size))
    # print(A)
    # print(np.linalg.norm(A, axis=0))
    A_normed = A / np.linalg.norm(A, axis=0)
    # print(A_normed)
    # print(np.sqrt(np.sum(A_normed[:, 1]**2)))
    conds.append(np.linalg.cond(A_normed))

print(np.min(conds), np.max(conds), np.median(conds), np.mean(conds))
plt.hist(conds, bins=100)
plt.show()

import numpy as np
from matplotlib import pyplot as plt
import matplotlib

matplotlib.use("TkAgg")

# A problem with a low condition number is said to be well-conditioned, while a problem with a high condition number is said to be ill-conditioned.


def generate_random_matrix(shape, normed=True, max_condition_number=10):
    if len(shape) != 2:
        raise ValueError()
    A = np.random.normal(size=(shape[0], shape[1]))
    if normed:
        A = A / np.linalg.norm(A, axis=0)
    condition_number = np.linalg.cond(A)
    if condition_number > max_condition_number:
        print(f"condition limit hit {condition_number}")
        A = generate_random_matrix(shape, normed, max_condition_number)
    return A


def random_radial_vector(length):
    theta = np.random.uniform(0, 2 * np.pi)
    x = length * np.cos(theta)
    y = length * np.sin(theta)
    return np.array([int(x), int(y)])


if __name__ == "__main__":
    vecs = []
    # for _ in range(4):
    #     vecs.append(generate_random_matrix((2, 1)))
    # assert np.vstack(vecs).shape == (8, 1)
    for _ in range(100):
        vecs.append(random_radial_vector(100))
    plt.plot([x[0] + 500 for x in vecs], [x[1] + 100 for x in vecs], '.')
    plt.show()

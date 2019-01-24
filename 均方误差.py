import numpy as np


def input_data(*args):
    data = np.array([arg for arg in args])
    avg = data.mean(axis=0)
    a = data - avg
    fz = 0
    fm = 0
    for i, k in zip(a[:, 0], a[:, 1]):
        fz = fz + i * k
        fm = fm + i ** 2
    b1 = fz / fm
    b0 = avg[1] - b1 * avg[0]
    print(b1, b0)


input_data([1, 14], [3, 24], [2, 18], [1, 17], [3, 27], [2,15])

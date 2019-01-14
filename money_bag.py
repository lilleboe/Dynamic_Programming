import numpy as np


def money_bag(money, value):
    x = [0] + money
    n = len(money)
    value += 1
    K = np.zeros((n, value))

    for i in range(1, n):
        for v in range(1, value):
            if x[i] <= v:
                K[i, v] = max((x[i] + K[i-1, v - x[i]]), K[i-1, v])
            else:
                K[i, v] = K[i-1, v]

    return K


if __name__ == '__main__':

    x = [1, 2, 5, 10, 20]
    y = 13

    print(money_bag(x, y))
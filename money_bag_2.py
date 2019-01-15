import numpy as np


def money_bag(money, value, max_coins):
    x = money
    n = len(money)
    value += 1
    max_coins += 1
    K = np.zeros((value, max_coins))
    K[0, :] = 1
    #print(K)

    for k in range(1, max_coins):
        for v in range(1, value):
            K[v, k] = 0
            for i in range(0, n):
                if x[i] <= v and K[v - x[i], k-1] == 1:
                    K[v, k] = 1

    #print(K)
    return K[-1, -1]


if __name__ == '__main__':

    x = [2, 5, 10, 20, 50]
    y = 87
    k = 4

    print(money_bag(x, y, k))
import numpy as np


def lp(classes):

    n = len(classes)
    dist = np.copy(classes)
    print(dist)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = max(dist[i][j], dist[i][k] + dist[k][j])

    print(dist)
    return int(dist.max()+1)


if __name__ == '__main__':
    i = -np.inf

    s = [[0, 1, i, i, i, i],
         [i, 0, 1, i, i, i],
         [i, i, 0, i, i, i],
         [i, i, i, 0, 1, i],
         [i, i, i, i, 0, i],
         [i, i, i, i, i, 0]]

    s = [[0, 1, i, 1, i, i, i, i],
         [i, 0, 1, i, i, i, i, i],
         [i, i, 0, 1, i, i, i, i],
         [i, i, i, 0, i, i, i, 1],
         [i, i, i, 1, 0, i, i, i],
         [i, i, i, i, i, 0, 1, i],
         [i, i, i, i, i, i, 0, i],
         [i, i, i, i, i, i, i, 0]]

    s = [[0, 1, 1, 1, i, i, i, i, i, i, i, i],
         [i, 0, i, i, 1, i, 1, i, i, i, i, i],
         [i, i, 0, 1, i, i, i, i, i, i, i, i],
         [i, i, i, 0, i, i, i, i, i, i, i, i],
         [i, i, i, i, 0, i, i, i, 1, i, i, i],
         [i, 1, i, i, i, 0, i, i, i, i, i, i],
         [i, i, i, i, i, i, 0, 1, i, i, i, i],
         [i, i, i, i, i, i, i, 0, i, i, i, i],
         [i, i, i, i, i, i, i, i, 0, 1, i, i],
         [i, i, i, i, i, i, i, i, i, 0, i, i],
         [1, i, i, i, i, i, i, i, i, i, 0, i],
         [i, i, i, i, i, i, i, i, i, i, i, 0]]

    print(s)
    print(lp(s))



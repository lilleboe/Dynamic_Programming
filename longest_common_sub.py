import numpy as np


def lcs(s1, s2):
    table = np.zeros((len(s1)+1, len(s2)+1))

    for i in range(0, len(s1)):
        for j in range(0, len(s2)):
            if s1[i] == s2[j]:
                table[i+1, j+1] = 1 + table[i, j]
            else:
                table[i+1, j+1] = table[i+1, j]
    print(table)
    return int(table.max())


if __name__ == '__main__':
    s1 = ['a', 'b', 'd', 'b', 'a', 'b', 'f', 'g', 'd']
    s2 = ['b', 'e', 't', 'f', 'd', 'b', 'f', 'a', 'f', 'r']
    print(s1)
    print(s2)
    print(lcs(s1, s2))

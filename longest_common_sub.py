import numpy as np


def lcs(s1, s2):
    sub1 = [''] + s1
    sub2 = [''] + s2

    table = np.zeros((len(sub1), len(sub2)))

    for i in range(1, len(sub1)):
        for j in range(1, len(sub2)):
            if sub1[i] == sub2[j]:
                table[i, j] = 1 + table[i-1, j-1]
            else:
                table[i, j] = table[i, j-1]
    #print(table)
    return int(table.max())


if __name__ == '__main__':
    str1 = ['a', 'b', 'd', 'b', 'a', 'b', 'f', 'g', 'd']
    str2 = ['b', 'e', 't', 'f', 'd', 'b', 'f', 'a', 'f', 'r']
    print(str1)
    print(str2)
    print(lcs(str1, str2))

    str1 = ['a', 'b', 'd', 'b', 'a', 'b', 'f', 'g', 'd']
    str2 = ['a', 'e', 'b', 'f', 'd', 'b', 'f', 'a', 'f', 'b']

    print(str1)
    print(str2)
    print(lcs(str1, str2))

    str1 = ['a', 'b', 'd', 'b', 'a', 'b', 'f', 'g', 'd']
    str2 = ['x', 'b', 'b', 'f', 'd', 'd', 'b', 'a', 'f', 'g']

    print(str1)
    print(str2)
    print(lcs(str1, str2))

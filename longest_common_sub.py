import numpy as np


def lcs(s1, s2):
    sub1 = [''] + s1
    sub2 = [''] + s2

    table = np.zeros((len(sub1), len(sub2)))
    max_value = 0

    for i in range(1, len(sub1)):
        for j in range(1, len(sub2)):
            if sub1[i] == sub2[j]:
                table[i, j] = 1 + table[i-1, j-1]
                if max_value < table[i, j]:
                    max_value = table[i, j]
            else:
                table[i, j] = table[i, j-1]
    #print(table)
    return int(max_value)


if __name__ == '__main__':
    str1 = ['a', 'b', 'd', 'b', 'a', 'b', 'f', 'g', 'd']
    str2 = ['b', 'e', 't', 'f', 'd', 'b', 'f', 'a', 'f', 'r']
    print("Calculated value: ", lcs(str1, str2))
    print("Expected value:   ", 4)
    print('-------------------')

    str1 = ['a', 'b', 'd', 'b', 'a', 'b', 'f', 'g', 'd']
    str2 = ['a', 'e', 'b', 'f', 'd', 'b', 'f', 'a', 'f', 'b']
    print("Calculated value: ", lcs(str1, str2))
    print("Expected value:   ", 6)
    print('-------------------')

    str1 = ['a', 'b', 'd', 'b', 'a', 'b', 'f', 'g', 'd']
    str2 = ['x', 'b', 'b', 'f', 'd', 'd', 'b', 'a', 'f', 'g']
    print("Calculated value: ", lcs(str1, str2))
    print("Expected value:   ", 4)
    print('-------------------')

    str1 = ['a', 'b', 'd', 'b', 'a', 'b', 'f', 'g', 'd']
    str2 = ['x', 'X', 'X', 'X', 'X', 'X', 'x']
    print("Calculated value: ", lcs(str1, str2))
    print("Expected value:   ", 0)
    print('-------------------')

    str1 = ['a', 'b', 'd', 'b', 'a', 'b', 'f', 'g', 'd']
    str2 = []
    print("Calculated value: ", lcs(str1, str2))
    print("Expected value:   ", 0)
    print('-------------------')

    str1 = []
    str2 = []
    print("Calculated value: ", lcs(str1, str2))
    print("Expected value:   ", 0)
    print('-------------------')

    str1 = []
    str2 = ['x', 'X', 'X', 'X', 'X', 'X', 'x']
    print("Calculated value: ", lcs(str1, str2))
    print("Expected value:   ", 0)
    print('-------------------')

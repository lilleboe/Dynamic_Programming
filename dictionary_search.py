import numpy as np


def dict_search(text_string, dictionary):

    n = len(text_string)
    results = [0] * (n+1)
    results[0] = 1
    word_salad = []

    for i in range(0, n):
        for j in range(0, i):
            #print(text_string[j:i+1], results)
            #print('------')
            if (results[j] == 1) and (text_string[j:i+1] in dictionary):
                results[i+1] = 1
                word_salad.append(text_string[j:i+1])
    return word_salad


if __name__ == '__main__':

    s = 'itwasthebestoftimes'
    d = ['it', 'was', 'the', 'best', 'of', 'times']

    print(dict_search(s, d))
